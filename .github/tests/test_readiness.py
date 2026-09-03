"""Exercise the actual workflow readiness command against local HTTP failures."""
import re
import shlex
import socket
import socketserver
import struct
import subprocess
import threading
import time
import unittest
from pathlib import Path


WORKFLOW = Path(__file__).resolve().parents[1] / "workflows" / "fly.yml"
MATCH = re.search(
    r"^\s*(curl [^\n]*http://127\.0\.0\.1:8000/healthz/)\s*$",
    WORKFLOW.read_text(),
    re.MULTILINE,
)
if MATCH is None:
    raise RuntimeError("Could not locate the workflow's container readiness command")
COMMAND = shlex.split(MATCH.group(1))


class ReadinessTests(unittest.TestCase):
    def run_probe(self, responses):
        class Handler(socketserver.BaseRequestHandler):
            def handle(self):
                self.request.settimeout(2)
                self.request.recv(8192)
                index = self.server.requests
                self.server.requests += 1
                response = responses[min(index, len(responses) - 1)]
                if response == "reset":
                    # Simulate Docker accepting the TCP connection before the app
                    # is ready: read the request, then send a TCP reset.
                    self.request.setsockopt(
                        socket.SOL_SOCKET, socket.SO_LINGER, struct.pack("ii", 1, 0)
                    )
                    self.request.close()
                elif response == "stall":
                    time.sleep(2)
                else:
                    status = "200 OK" if response == "ok" else "503 Unavailable"
                    self.request.sendall(
                        f"HTTP/1.1 {status}\r\nContent-Length: 2\r\nConnection: close\r\n\r\nok".encode()
                    )

        with socketserver.ThreadingTCPServer(("127.0.0.1", 0), Handler) as server:
            server.daemon_threads = True
            server.requests = 0
            worker = threading.Thread(target=server.serve_forever, daemon=True)
            worker.start()
            command = COMMAND[:-1] + [
                # Shorter budgets keep regression tests fast. Retry semantics
                # (--retry-all-errors and --fail) come from the workflow unchanged.
                "--retry", "2", "--retry-delay", "1", "--retry-max-time", "4",
                "--connect-timeout", "1", "--max-time", "1",
                f"http://127.0.0.1:{server.server_address[1]}/healthz/",
            ]
            started = time.monotonic()
            try:
                result = subprocess.run(
                    command, capture_output=True, text=True, timeout=8
                )
                return result, server.requests, time.monotonic() - started
            finally:
                server.shutdown()
                worker.join(timeout=2)

    def test_reset_then_unavailable_then_ready(self):
        result, requests, _ = self.run_probe(["reset", "unavailable", "ok"])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(requests, 3)
        # curl can report an early connection close as an empty reply (52)
        # or receive/reset failure (56), depending on the OS and socket timing.
        self.assertRegex(result.stderr, r"curl: \((52|56)\)")

    def test_permanent_failure_still_fails(self):
        result, requests, elapsed = self.run_probe(["unavailable"])
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(requests, 3)
        self.assertLess(elapsed, 8)

    def test_hung_request_is_bounded(self):
        result, _, elapsed = self.run_probe(["stall"])
        self.assertNotEqual(result.returncode, 0)
        self.assertLess(elapsed, 8)

    def test_production_command_has_time_bounds(self):
        for flag, maximum in (
            ("--retry", 15), ("--retry-max-time", 60),
            ("--connect-timeout", 2), ("--max-time", 5),
        ):
            self.assertIn(flag, COMMAND)
            self.assertGreater(float(COMMAND[COMMAND.index(flag) + 1]), 0)
            self.assertLessEqual(float(COMMAND[COMMAND.index(flag) + 1]), maximum)


if __name__ == "__main__":
    unittest.main(verbosity=2)
