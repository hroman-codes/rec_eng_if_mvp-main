"""Isolated test settings: never load local credentials or contact production."""
import os

os.environ['DJANGO_READ_DOT_ENV'] = 'false'
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'
os.environ['SENTRY_DSN'] = ''
os.environ['SECRET_KEY'] = 'linktag-tests-only-not-for-production'
os.environ['DEBUG'] = 'false'

from .settings import *  # noqa: E402,F403

PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
