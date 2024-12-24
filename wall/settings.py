import os
from pathlib import Path
import dj_database_url

# Base directory for the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# Debug settings
DEBUG = True

# URLs and Hosts
ROOT_URLCONF = 'wall.urls'
WSGI_APPLICATION = 'wall.wsgi.application'
CSRF_TRUSTED_ORIGINS = ['https://wall-87216da9fac5.herokuapp.com']
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'wall-87216da9fac5.herokuapp.com']



# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'accounts',
    'storages',
    'gunicorn',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'accounts.context_processors.profile_context',
            ],
        },
    },
]

# Alert Messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# Database settings
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Auth
AUTH_USER_MODEL = 'accounts.Profile'

# Validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Initializing
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Email Config.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')


# Static files settings
STATIC_URL = '/static/'

if 'USE_AWS' in os.environ:
    # AWS S3 configuration for static files
    AWS_STORAGE_BUCKET_NAME = 's3-bucket-wall'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'

    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

    # Static files directory for AWS S3
    STATICFILES_DIRS = [BASE_DIR / 'static']
    STATIC_ROOT = BASE_DIR / 'staticfiles'
else:
    # Local development (default Django static serving)
    STATICFILES_DIRS = [BASE_DIR / 'static']
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    if DEBUG:
        STATIC_URL = '/static/'

# Media files settings
MEDIA_URL = '/media/'

if 'USE_AWS' in os.environ:
    # AWS S3 configuration for media files
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

    # Ensure media files are uploaded under the 'media/' folder in S3 bucket
    MEDIAFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

else:
    # Local development (default Django media handling)
    MEDIA_ROOT = BASE_DIR / 'media'
    MEDIA_URL = '/media/'  # For local development