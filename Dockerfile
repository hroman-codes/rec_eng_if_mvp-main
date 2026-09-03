# Build the React homepage and copy the shared Django design assets.
FROM node:22-bookworm-slim AS frontend
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY public/ public/
COPY src/ src/
COPY static/ static/
COPY prepare-frontend.cjs ./
RUN npm run build

FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_READ_DOT_ENV=false \
    DEBUG=false
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY manage.py .
COPY apps/ apps/
COPY rec_eng_if_mvp/ rec_eng_if_mvp/
COPY templates/ templates/
COPY static/ static/
# settings.py loads index.html from /app/build and bundles from /app/build/static.
COPY --from=frontend /app/build /app/build
# Build-time values are deliberately non-production and apply only to this command.
RUN SECRET_KEY=build-only-placeholder DATABASE_URL=sqlite:///:memory: SENTRY_DSN= python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["gunicorn", "rec_eng_if_mvp.wsgi:application", "--bind", "0.0.0.0:8000", "--access-logfile", "-"]
