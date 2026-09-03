# Linktag Django/React integration — visual QA

final result: passed

## Comparison target and evidence

The implementation target is the approved, runnable option-3 preview, not a
pixel-identical recreation of the original generated board. Its already-reviewed
artwork and navy/blue design were carried into the real Django application.

Source visual truth:
`/Users/hroman_codes/Documents/Code/rec_eng_if_mvp-main/docs/design/linktag-preview/qa/`

- `home-normalized.png`
- `signin-normalized.png`
- `register-normalized.png`
- `dashboard-normalized.png`

Original direction board:
`/Users/hroman_codes/.codex/generated_images/01a06394-3fe2-72e0-9115-5d86ea77790a/exec-534f6791-0962-40bf-bca8-e31ad9b41ef1.png`

Browser-rendered implementation:
`http://127.0.0.1:8001/`, using Django/Gunicorn, the production React build,
WhiteNoise, and an isolated temporary SQLite database. No production data was used.

Implementation evidence:
`/Users/hroman_codes/Documents/Code/rec_eng_if_mvp-main/docs/design/django-integration/qa/`

- Final desktop captures: `home-desktop-final.png`, `signin-desktop-final.png`,
  `register-desktop-final.png`, `dashboard-desktop-final.png`.
- Normalized comparisons: `home-final-normalized.png`, `signin-final-normalized.png`,
  `register-final-normalized.png`, `dashboard-final-normalized.png`.
- Focused form comparison: `signin-source-detail.png` and `signin-final-detail.png`.
- Responsive evidence: `home-mobile-final.png`, `signin-mobile.png`,
  `register-mobile.png`, `dashboard-mobile.png`, `dashboard-tablet.png`.
- Additional states: `upload-desktop.png` and `signin-error.png`.

Each source/implementation pair was opened together in the same image-comparison
input. The sign-in control region was also compared at a larger, readable scale.
Desktop dashboard captures were inspected at full size for table and detail readability.

## Viewports and normalization

Desktop CSS viewport: 1440 × 980, browser devicePixelRatio approximately 1.4.
The in-app browser capture includes a scaled 1028 × 700 content region inside a
1440 × 980 image, with blank capture padding outside that region. That padding is
a capture artifact, not page overflow. The actual content region was cropped at
offset (1, 1), then resized to 720 × 490 to match the source captures.

Focused sign-in images are 385 × 250 crops of those normalized images.
Mobile CSS viewport: 390 × 844. Tablet CSS viewport: 768 × 1024.
DOM measurements confirmed no document-level horizontal overflow on all four mobile
pages and the tablet dashboard. Temporary viewport overrides were reset afterward.

States: empty authentication forms; logged-in dashboard with four fictional,
database-backed contacts and four selected tags; successful note save; failed login.
The source dashboard has five fictional contacts and three tags, so content-dependent
row counts, wrapping, and detail heights were not treated as pixel mismatches.

## Findings and comparison history

1. Initial comparison — blocked:
   - [P2] Form hints were missing, unlike the approved preview; registration also
     auto-focused email, skipping the name fields and moving the mobile viewport.
     Fixed with placeholders, appropriate autocomplete, and removal of autofocus.
   - [P2] A CSS filter made the original blue logo white. Removed the filter and
     restored the actual shared logo asset.
   - [P2] Homepage illustration density differed because it contained four rows
     instead of the preview's five. Restored the five-row illustration.

2. Post-fix homepage comparison — blocked:
   - [P2] A shared `#page-content` rule overrode the hero's bottom padding and
     shifted its vertical alignment. Gave the React hero its own skip-link target,
     `#home-content`, so the original hero spacing rules apply.

3. Final comparison — passed:
   - Final normalized captures confirm restored logo, form hints, five-row
     homepage density, and matching hero alignment.
   - The focused sign-in comparison confirms field spacing, control heights,
     typography, and action placement.
   - No actionable P0/P1/P2 differences remain against the approved preview.

## Required fidelity surfaces

- Typography: self-hosted Inter 400/500/600/700, original headline hierarchy,
  line breaks, weights, and button sizing retained. Long contact values wrap.
- Spacing/layout: navy hero, split authentication pages, 254px desktop sidebar,
  recommendation table, and right-hand detail panel retain the approved proportions.
  Mobile stacks content; tablet moves details below the table.
- Colors/tokens: original navy, blue, pale-blue selection, yellow accent, and
  blue logo restored. Focus, validation, and notification states remain distinct.
- Image/asset fidelity: actual existing SVG logo and generated tag artwork reused.
  No hand-drawn replacements. Artwork retains the preview's crop and resolution.
  Standard icon libraries are used for real controls.
- Copy/content: preview warnings and fake policy dialogs removed. Real links lead
  to Django routes. Added truthful password guidance, import constraints, result
  counts, and session-based tag guidance.

## Intentional production differences

- Homepage/footer use illustrative names and the existing creator link rather than
  nonfunctional Privacy/Terms/Contact preview dialogs.
- Added an Import connections navigation item.
- Contact names, company names, notes, and counts come from the signed-in user's database.
- Editing uses a keyboard-accessible inline form instead of a mock modal.
- Tags are stored in the existing Django session, not React demo memory.
- Registration includes the real password requirements.
- Authentication and state-changing actions use real POST forms with CSRF protection.
- The preview navigation strip is absent.

## Interaction and verification checklist

- [x] Home links open real sign-in and registration pages.
- [x] Registration creates a local test account and opens import.
- [x] Sign-in, incorrect-password errors, visibility toggle, and POST sign-out work.
- [x] Adding tags updates database-backed recommendations.
- [x] Contact selection, editing, and note saving work in the browser.
- [x] Saved browser note independently verified in the isolated database.
- [x] Django tests cover CSV imports, malformed/oversized files, re-import preservation,
  tag limits/removal, empty states, ownership restrictions, and CSRF enforcement.
- [x] Mobile and tablet layouts inspected; no horizontal overflow found.
- [x] Browser error logs checked: no errors reported.
- [x] 51 Django tests and 2 React tests pass; production build and static collection pass.
- [x] Fly configuration validates; workflow YAML parses.

## Remaining gaps and follow-up polish

- [P3] Django's Bootstrap icon font has small stroke differences from the React
  preview's Phosphor icons; standard icons are complete and aligned.
- [P3] Tag artwork retains the approved preview's softer contrast relative to the
  original generated board.
- Desktop validation passed locally on Python 3.9 / Node 26; CI is configured for
  production Python 3.11 / Node 22.
- The native file-picker interaction was not automated; multipart CSV import behavior
  is covered by Django tests.
- Docker is not installed locally. Its build/smoke check will first run in GitHub Actions.
- No live Fly deployment has been performed. See `docs/deployment.md` for deployment
  instructions, token rotation, and existing dependency-maintenance warnings.
