import { ArrowRight, CheckCircle, PlayCircle, Tag, UploadSimple, Users } from '@phosphor-icons/react';

const examples = [
  { initials: 'JL', name: 'Jordan Lee', company: 'Acme Studio', position: 'Software engineer' },
  { initials: 'AM', name: 'Alex Morgan', company: 'Northstar', position: 'Product manager' },
  { initials: 'SC', name: 'Sam Chen', company: 'Forma', position: 'UX designer' },
  { initials: 'RP', name: 'Riley Patel', company: 'Orbit Labs', position: 'Founder' },
  { initials: 'CS', name: 'Casey Smith', company: 'Fieldwork', position: 'Product designer' },
];
const steps = [
  { Icon: UploadSimple, title: '1. Upload your CSV', copy: 'Export your connections from LinkedIn and upload your CSV file.' },
  { Icon: Tag, title: '2. Choose your tags', copy: 'Select up to five role tags that represent the people you want to find.' },
  { Icon: Users, title: '3. Find your people', copy: 'Match your connections with your tags, so you can focus on the right people.' },
];

export default function App() {
  return <div className="home-page">
    <a className="skip-link" href="#home-content">Skip to content</a>
    <section className="home-dark">
      <header className="home-header">
        <a href="/" className="logo" aria-label="Linktag home"><img src="/static/images/user-tag-solid.svg" alt="" />Linktag</a>
        <nav aria-label="Main navigation"><a href="/seeker/login/">Sign in</a><a href="/seeker/register/" className="button">Create account</a></nav>
      </header>
      <main id="home-content" className="hero">
        <div className="hero-copy">
          <p className="eyebrow">A clearer view of your network</p>
          <h1>Your network.<br />The right people.</h1>
          <p className="hero-description">Find the connections that matter. Upload your LinkedIn CSV, choose your role tags, and explore your matches.</p>
          <div className="hero-actions"><a href="/seeker/register/" className="button">Get started <ArrowRight size={18} /></a><a className="text-action" href="#how-it-works"><PlayCircle size={24} />See how it works</a></div>
        </div>
        <div className="hero-product" aria-label="Illustrative connections, not real customer data">
          <div className="preview-table">
            <div className="preview-row preview-head"><span>Person</span><span>Company</span><span>Position</span><span /></div>
            {examples.map((person, index) => <div className="preview-row" key={person.name}>
              <span className="person-cell"><span className={`avatar tone-${index}`} aria-hidden="true">{person.initials}</span><strong>{person.name}</strong></span>
              <span>{person.company}</span><span>{person.position}</span><CheckCircle size={18} className="match-check" aria-label="Matched" />
            </div>)}
          </div>
        </div>
      </main>
    </section>
    <section id="how-it-works" className="how-it-works" aria-label="How it works">
      {steps.map(({ Icon, title, copy }) => <div className="step" key={title}><span className="step-icon"><Icon size={30} aria-hidden="true" /></span><div><h2>{title}</h2><p>{copy}</p></div></div>)}
    </section>
    <footer className="footer"><span>© {new Date().getFullYear()} Linktag</span><span>Built by <a href="https://github.com/hroman-codes">hroman_codes</a> · Not affiliated with LinkedIn</span></footer>
  </div>;
}
