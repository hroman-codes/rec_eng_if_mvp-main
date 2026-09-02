export const initialTags = ['Software Engineer', 'Product Manager', 'UX Designer'];
export const initialPeople = [
  { id: 1, firstName: 'Maya', lastName: 'Chen', company: 'Northstar', position: 'Software Engineer', email: 'maya@example.com', bio: 'Full-stack engineer passionate about building scalable web applications and improving developer experiences. Currently focused on platform infrastructure and tooling.', notes: 'Met at Product Meetup SF. Interested in mentorship and opportunities in platform engineering.' },
  { id: 2, firstName: 'Daniel', lastName: 'Brooks', company: 'Forma', position: 'Product Manager', email: 'daniel@example.com', bio: 'Product manager building thoughtful collaboration tools for growing teams.', notes: 'Ask about the product discovery workshop.' },
  { id: 3, firstName: 'Sofia', lastName: 'Patel', company: 'Studio Eight', position: 'UX Designer', email: 'sofia@example.com', bio: 'Designer working at the intersection of research, accessibility, and product strategy.', notes: 'Interested in sharing design-system resources.' },
  { id: 4, firstName: 'Alex', lastName: 'Morgan', company: 'Arc', position: 'Software Engineer', email: 'alex@example.com', bio: 'Software engineer focused on frontend architecture and accessible interfaces.', notes: 'Follow up about the frontend community.' },
  { id: 5, firstName: 'Jordan', lastName: 'Lee', company: 'Fieldwork', position: 'Product Manager', email: 'jordan@example.com', bio: 'Helping small teams turn customer insights into useful products.', notes: 'Enjoys talking about early-stage product strategy.' },
];
export function filterPeople(people, tags) { return people.filter(p => tags.some(tag => p.position.toLowerCase().includes(tag.toLowerCase()))); }
// Supports quoted commas/newlines and LinkedIn's optional preamble.
export function parseConnections(text) {
  const rows = []; let row = [], cell = '', quoted = false;
  for (let i = 0; i < text.length; i++) { const ch = text[i]; if (ch === '"') { if (quoted && text[i + 1] === '"') { cell += '"'; i++; } else quoted = !quoted; } else if (ch === ',' && !quoted) { row.push(cell.trim()); cell = ''; } else if ((ch === '\n' || ch === '\r') && !quoted) { if (ch === '\r' && text[i + 1] === '\n') i++; row.push(cell.trim()); if (row.some(Boolean)) rows.push(row); row = []; cell = ''; } else cell += ch; }
  if (quoted) throw new Error('This CSV has an unclosed quoted field. Please check the file.');
  row.push(cell.trim()); if (row.some(Boolean)) rows.push(row);
  const headerIndex = rows.findIndex(r => r.map(v => v.replace(/^\uFEFF/, '').toLowerCase()).includes('first name') && r.some(v => v.toLowerCase() === 'position'));
  if (headerIndex < 0) throw new Error('We couldn’t find LinkedIn column headers. Include First Name, Last Name, Company, and Position.');
  const header = rows[headerIndex].map(v => v.replace(/^\uFEFF/, '').toLowerCase());
  if (!['first name', 'last name', 'company', 'position'].every(key => header.includes(key))) throw new Error('The CSV needs First Name, Last Name, Company, and Position columns.');
  const value = (r, key) => r[header.indexOf(key)] || '';
  const people = rows.slice(headerIndex + 1).filter(r => value(r, 'first name') || value(r, 'last name')).map((r, index) => ({ id: index + 1, firstName: value(r, 'first name'), lastName: value(r, 'last name'), company: value(r, 'company'), position: value(r, 'position'), email: value(r, 'email address'), bio: '', notes: '' }));
  if (!people.length) throw new Error('This CSV has headers but no connections. Try a file with connection rows.'); return people;
}
