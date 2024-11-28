from datetime import timedelta
from pathlib import Path

from decouple import config

######################################################################
# General
######################################################################
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', False)

ALLOWED_HOSTS = ['localhost', 'api', '127.0.0.1']

WSGI_APPLICATION = 'core.wsgi.application'

ROOT_URLCONF = 'core.urls'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

######################################################################
# Apps
######################################################################
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'django_filters',
    'corsheaders',
    'huey.contrib.djhuey',
    'apps.authentication',
    'apps.achievements',
    'apps.items',
    'apps.inventory',
    'apps.equipment',
    'apps.skills',
    'apps.combat',
    'apps.actions',
    'apps.quests',
    'apps.market',
    'apps.state',
    'apps.logs',
]

######################################################################
# Middleware
######################################################################
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

######################################################################
# Templates
######################################################################
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

######################################################################
# Database
######################################################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        #         'ENGINE': 'django.db.backends.postgresql',
        #         'NAME': config('DB_NAME'),
        #         'USER': config('DB_USER', 'postgres'),
        #         'PASSWORD': config('DB_PASSWORD', 'password'),
        #         'HOST': config('DB_HOST', 'localhost'),
        #         'PORT': config('DB_PORT', '5432'),
    }
}

######################################################################
# Authentication
######################################################################
AUTH_USER_MODEL = 'authentication.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

######################################################################
# Internationalization
######################################################################
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

######################################################################
# Staticfiles
######################################################################
STATIC_URL = 'static/'

######################################################################
# Rest Framework
######################################################################
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'core.paginations.CustomPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'drf_orjson_renderer.renderers.ORJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'drf_orjson_renderer.parsers.ORJSONParser',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'TOKEN_OBTAIN_SERIALIZER': 'apps.authentication.serializers.CustomTokenObtainPairSerializer',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'IDLE GAME API',
    'DESCRIPTION': 'by Squies',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

######################################################################
# huey
######################################################################
HUEY = {
    'results': True,
    'huey_class': 'huey.SqliteHuey',
    'filename': config('HUEY_DB_PATH', 'huey_db/huey.db'),
    'immediate': False,
    'consumer': {
        'workers': 1,
        'worker_type': 'process',
    }
}

if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOW_CREDENTIALS = True
    CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:5173']
