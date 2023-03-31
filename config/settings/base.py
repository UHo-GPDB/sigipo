"""
Settings common to all instances of the project

Generated by 'django-admin startproject' using Django 3.2.4.
"""
import os
from pathlib import Path

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).parent.parent.parent

load_dotenv(dotenv_path=BASE_DIR / ".env")

SECRET_KEY = os.environ.get("SECRET_KEY", None)

# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "django.forms",
]

THIRD_PARTY_APPS = [
    "django_version_checks",
    "django_filters",
    "django_select2",
]

LOCAL_APPS = [
    "apps.accounts.apps.AccountsConfig",
    "apps.core.apps.CoreConfig",
    "apps.geographic_location.apps.GeographicLocationConfig",
    "apps.patient.apps.PatientConfig",
    "apps.classifiers.apps.ClassifiersConfig",
    "apps.dashboard.apps.DashboardConfig",
    "apps.cancer_registry.apps.CancerRegistryConfig",
    "apps.drugs.apps.DrugsConfig",
    "apps.nuclear_medicine.apps.NuclearMedicineConfig",
    "apps.chemotherapy.apps.ChemotherapyConfig",
    "apps.employee.apps.EmployeeConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "apps.core.middleware.UserBasedExceptionMiddleware",
]

ROOT_URLCONF = "config.urls"

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "sigipo/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", None),
        "USER": os.environ.get("POSTGRES_USER", None),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", None),
        "HOST": os.environ.get("POSTGRES_DB_HOST", None),
        "PORT": os.environ.get("POSTGRES_DB_PORT", None),
    },
}

# Database for Github Tests

if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "github_actions",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "es-es"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# languages list
LANGUAGES = [
    ("es", "Spanish"),
    ("en", "English"),
]

# User model
AUTH_USER_MODEL = "accounts.User"

VERSION_CHECKS = {
    "python": ">=3.10.0,<3.12.0",
}

SELECT2_JS = ""
SELECT2_CSS = ""
SELECT2_I18N_PATH = ""

LOGIN_REDIRECT_URL = "/"

EMAIL_HOST = os.environ.get("EMAIL_HOST", None)

EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD", None)

EMAIL_HOST_USER = os.environ.get("EMAIL_USER", None)

EMAIL_PORT = os.environ.get("EMAIL_PORT", None)

DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", None)

FORM_RENDERER = "django.forms.renderers.TemplatesSetting"
