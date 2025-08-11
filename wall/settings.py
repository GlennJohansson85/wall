import os
from pathlib import Path
if os.path.isfile('env.py'):
    import env

from django.contrib.messages import constants as messages
from cloudinary import uploader


BASE_DIR             = Path(__file__).resolve().parent.parent
SECRET_KEY           = os.environ.get('SECRET_KEY', '')
DEBUG                = True
ROOT_URLCONF         = 'wall.urls'
WSGI_APPLICATION     = 'wall.wsgi.application'
CSRF_TRUSTED_ORIGINS = ['https://wall-2bb3003277ac.herokuapp.com/']
ALLOWED_HOSTS        = ['localhost', '127.0.0.1', 'wall-2bb3003277ac.herokuapp.com']

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
    'cloudinary',
    'cloudinary_storage',
    'gunicorn',
    'whitenoise.runserver_nostatic',
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
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME'  : BASE_DIR / 'db.sqlite3',
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
TIME_ZONE     = 'UTC'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True

# Email Config.
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS       = True
EMAIL_PORT          = 587
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_HOST_USER     = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# Static files settings for local development
STATIC_URL       = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT      = os.path.join(BASE_DIR, 'staticfiles')

# Disable caching of static files in development (important for CSS changes)
WHITENOISE_MAX_AGE =    0  # Set to 0 during development to avoid caching

# Cloudinary will handle the media
MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR /'media'

# Media files (Cloudinary)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY'   : os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
