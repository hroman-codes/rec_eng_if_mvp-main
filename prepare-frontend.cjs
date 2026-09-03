// Django and React share the same design assets. public/static is generated.
const fs = require('node:fs');
const path = require('node:path');
const source = path.join(__dirname, 'static');
const destination = path.join(__dirname, 'public/static');
fs.mkdirSync(destination, { recursive: true });
for (const folder of ['css', 'fonts', 'images']) {
  fs.cpSync(path.join(source, folder), path.join(destination, folder), { recursive: true });
}
