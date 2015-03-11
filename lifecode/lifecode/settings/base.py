"""
Django settings for lifecode project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cf#3wb6f0*zh^g=n7cgl+^3)4tsj6v@f+xg_9ga764%^66t%!5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
REQ_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'corsheaders',
]

PROJECT_APPS = [
    'orm',
    'user',
    'blog',
    'media',
]

INSTALLED_APPS = REQ_APPS + PROJECT_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

#Django Rest Framework
REST_FRAMEWORK = {
    'PAGINATE_BY':6,                # Default to 10
    'PAGINATE_BY_PARAM': 'page_limit',  # Allow client to override, using `?page_size=xxx`.
    'MAX_PAGINATE_BY': 100,             # Maximum limit allowed when using `?page_size=xxx`.
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}

#CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'api.lifecode.loc'
    # Here was the problem indeed and it has to be http://localhost:3000,
    # not http://localhost:3000/
)

ROOT_URLCONF = 'lifecode.urls'

WSGI_APPLICATION = 'lifecode.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lifecode_blog',
        'USER': 'root',
        'PASSWORD': '1261',
        'HOST': 'localhost',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
BASE_PATH = os.path.abspath(os.path.join(BASE_DIR, '../'))
# BASE_PATH = os.path.dirname(os.path.abspath(''))
STATIC_ROOT = os.path.join(BASE_PATH, 'static')
STATIC_URL = '/static/'


# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
FILE_UPLOAD_MAX_MEMORY_SIZE=214958080
#UPLOAD Configuration
UPLOAD_ROOT = os.path.join(BASE_PATH, 'upload')
UPLOAD_URL = 'upload/'

UPLOAD_IMAGE_ROOT = os.path.join(UPLOAD_ROOT, 'image')
UPLOAD_AUDIO_ROOT = os.path.join(UPLOAD_ROOT, 'audio')
UPLOAD_VIDEO_ROOT = os.path.join(UPLOAD_ROOT, 'video')
UPLOAD_OTHER_ROOT = os.path.join(UPLOAD_ROOT, 'other')

UPLOAD_IMAGE_URL = os.path.join(UPLOAD_URL, 'image')
UPLOAD_AUDIO_URL = os.path.join(UPLOAD_URL, 'audio')
UPLOAD_VIDEO_URL = os.path.join(UPLOAD_URL, 'video')
UPLOAD_OTHER_URL = os.path.join(UPLOAD_URL, 'other')
