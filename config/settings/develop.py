"""
This is the settings file that you use when you're working on the project locally.
Local development-specific include DEBUG mode, log level, and activation of developer tools like django-debug-toolsbar
"""

# flake8: noqa
from config.settings.base import *  # unimport:skip

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "qov#ce&bl3z8@ymehv1byt^beru%el-0wjo%e#1q8#og6331ik"

ALLOWED_HOSTS = ["*"]

MEDIA_ROOT = os.path.join(BASE_DIR, "sigipo", "media")

# email settings
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

THIRD_PARTY_APPS = ["django_linear_migrations", "django_extensions", "debug_toolbar"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]
