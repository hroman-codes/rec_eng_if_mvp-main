# Django/React integration and automatic deployment

The production app is still Django. React renders the homepage; Django renders
sign-in, registration, recommendations, CSV import, tags, and contact editing.
The separate prototype under `docs/design/linktag-preview` is not deployed.

## What a push does

Push this change (including `.github/workflows/fly.yml`) to `main` in
`hroman-codes/link_tag`. GitHub Actions will:

1. Run the Django suite against an isolated SQLite test database and check for missing migrations.
2. Run React tests and build the homepage using Node 22.
3. Build the production Docker image and smoke-test Django, the homepage, and static assets.
4. Deploy to the existing Fly app `linktag` only if all checks pass.
5. Run the existing migration release command and verify `/healthz/`.

Pull requests run checks but do not deploy. Manual runs deploy only when the selected
branch is `main`. Pipelines for the same branch are serialized to avoid stale deployments.
No commit, push, or live deployment was performed during configuration.

Repository Actions: https://github.com/hroman-codes/link_tag/actions

Live application: https://linktag.fly.dev/

## Credentials

- GitHub repository secret `FLY_API_TOKEN` was configured and its presence verified.
- It is a deploy token scoped to the `linktag` app, named `github-actions-link-tag`.
- The token was created on September 2, 2026 with a one-year expiry. Rotate it before September 2, 2027.
- Existing Fly secrets `SECRET_KEY`, `DATABASE_URL`, and `SENTRY_DSN` remain on Fly.
- No secret values are committed or embedded in the image. CI and image builds use dummy settings.

For rotation, generate an app-scoped deploy token and replace the encrypted GitHub
`FLY_API_TOKEN` secret. Do not paste token values into source files or logs.
See the [Fly GitHub Actions guide](https://fly.io/docs/launch/continuous-deployment-with-github-actions/)
and [deploy-token documentation](https://fly.io/docs/flyctl/tokens-create-deploy/).

## Local checks

Use Python 3.11 and Node 22 to match the image and CI:

```sh
python -m pip install -r requirements.txt
python manage.py test apps/seeker/tests --settings=rec_eng_if_mvp.test_settings --noinput
python manage.py makemigrations --check --dry-run --settings=rec_eng_if_mvp.test_settings
npm ci
CI=true npm test -- --watchAll=false --runInBand
CI=true npm run build
flyctl config validate --config fly.toml
```

`test_settings` disables reading `.env`, disables Sentry, and uses in-memory SQLite.
Do not run tests with production settings or a production database URL.

For local manual use, explicitly set `DJANGO_READ_DOT_ENV=false`, a local-only
`SECRET_KEY`, `DATABASE_URL` pointing to a local SQLite database, `SENTRY_DSN=`,
and `DEBUG=true` before migrations or `runserver`.

## Shared design assets

- Canonical CSS: `static/css/linktag.css`.
- Self-hosted Inter fonts, icon font, logo, and generated tag artwork: `static/`.
- `prepare-frontend.cjs` copies shared assets to ignored `public/static/` before React builds.
- The image copies React's build to `/app/build`, which matches Django's template/static settings.
- `collectstatic` gathers bundles and source assets into `/app/staticfiles`.
  Duplicate shared-asset notices are expected: Django takes the canonical `static/` copy first.
- CSV imports validate before writing; contact views and edits are scoped to the signed-in owner.
- Role tags retain the existing session-based lifetime and are cleared when signing out.
- Dashboard results show the first 50 matches, with total counts and guidance to narrow tags.

## Verification and remaining maintenance

Local verification passed: 51 Django tests, 2 React tests, production React build,
static collection, Fly configuration validation, and browser checks of the integrated app.
Local Python was 3.9 and Node was 26; CI uses Python 3.11 and Node 22.
Docker is unavailable on this workstation, so the container smoke test will first
execute in GitHub Actions. The first live deployment has not yet been verified.

The existing Create React App toolchain is unmaintained. The dependency installer
reported 68 audit findings across the dependency tree (15 low, 16 moderate,
34 high, 3 critical). No blanket or breaking dependency upgrades were applied.
Plan a separate dependency modernization/security review; these counts do not
establish exploitability in the deployed application. Django also remains on the
repository's existing pinned version.

If deployment fails, inspect the Actions job logs before retrying. Do not reset or
recreate the production database. Reverting the relevant source commit and pushing
to main redeploys the reverted application; database rollback needs separate review.
