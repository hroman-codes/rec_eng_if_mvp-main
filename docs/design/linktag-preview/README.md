# Linktag — option 3 interactive preview

An isolated React/Vite prototype of the selected navy-and-blue direction. The existing React homepage, Django templates, database, authentication, and production assets are unchanged.

## Preview

`npm install` then `npm run dev -- --host 127.0.0.1 --port 4173 --strictPort`.

Use the bottom preview navigation to visit Home, Sign in, Register, and Dashboard. Demo sign-in accepts any nonempty sample password and valid-format email; it does not authenticate. Do not enter real credentials.

Registration demonstrates field validation, optional CSV import, role selection, and recommendations. CSVs are parsed only in browser memory; no network upload occurs. Tag filtering, contact selection, editable notes and details, account menu, sign-out, and empty states work. All state resets on reload. There is no real account creation, persistence, messaging, or LinkedIn integration. Privacy/Terms/Contact buttons explain the preview scope rather than presenting invented production policies.

## Verify

`npm run build`

`node --test tests/data.test.mjs`

`npm run test:sites`

See `design-qa.md` and `qa/` for browser captures and comparison notes.

## Assets and design

- Source of truth: third displayed image from the design exploration, saved in this task's generated_images directory as `exec-534f6791-0962-40bf-bca8-e31ad9b41ef1.png`; reference quadrants are retained in `qa/`.
- Brand logo: existing project asset, copied without modification to `public/assets/linktag.svg`.
- Icons: Phosphor React, using a consistent lightweight outline treatment.
- Typeface: self-hosted Inter via Fontsource; no external font requests.
- Decorative asset: `public/assets/tag-art.png`, generated with the built-in image tool. Prompt: “600 × 420 decorative auth sidebar asset on solid #061c34 navy; overlapping thin azure-blue and muted-yellow outlined tilted tags; small sparse blue dots; centered motif, ample margins; no text, UI, or logo.” Generated at 1499 × 1049, displayed responsively without stretching.

Integration into the live Django/React app is a separate next step; this prototype intentionally does not replace production routes or change backend behavior.
