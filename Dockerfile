# Stage 1: Build front-end assets
FROM node:16 as build-stage
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy all frontend source files
COPY public/ public/
COPY src/ src/
COPY *.js ./
COPY *.json ./

# Build frontend
RUN npm run build

# Stage 2: Set up Django with built assets
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project files
COPY manage.py .
COPY apps/ apps/
COPY rec_eng_if_mvp/ rec_eng_if_mvp/
COPY templates/ templates/
COPY static/ static/
COPY staticfiles/ staticfiles/

# Copy built assets from build stage to Django static directory
COPY --from=build-stage /app/build /app/staticfiles/build

# Collect static files
RUN python manage.py collectstatic --noinput

# Make sure static files directory is accessible
RUN chmod -R 755 /app/staticfiles

# Expose port
EXPOSE 8000

# Run gunicorn
CMD gunicorn rec_eng_if_mvp.wsgi:application --bind 0.0.0.0:8000