"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from moear_api_common import utils
from django.utils.translation import gettext_noop
from django.contrib import messages
from kombu import Queue, Exchange


# 创建辅助用的工具函数
def _get_config(name, default=None):
    return os.environ.get(name, default)


def _get_config_int(name, default):
    assert isinstance(default, int)
    return int(_get_config(name, default))


def _get_config_bool(name, default):
    assert isinstance(default, bool)
    default = 'true' if default else 'false'
    return _get_config(name, default).lower() == 'true'


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNTIME_DIR = os.path.join(BASE_DIR, '..', 'runtime')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = _get_config(
    'SECRET_KEY',
    '7_%wji=lxr3)@1r17t$!@7z%q$kk7_sxb&i#tiadby^5la%tua')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = _get_config_bool('DEBUG', True)
PRODUCTION = _get_config_bool('PRODUCTION', False)

ALLOWED_HOSTS = _get_config(
    'ALLOWED_HOSTS',
    'localhost,127.0.0.1').split(',')


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 第三方库
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'invitations',
    'rest_framework',
    'django_celery_beat',

    # 当前项目实现
    'posts.apps.PostsConfig',
    'spiders.apps.SpidersConfig',
    'core.apps.CoreConfig',
    'terms.apps.TermsConfig',
    'deliver.apps.DeliverConfig',
    'pages.apps.PagesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'server.wsgi.application'


# 身份认证后端配置
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(
                BASE_DIR, 'server', 'config', 'db', 'mysql.conf'
            ),
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
        'TEST': {
            'NAME': _get_config('TEST_DATABASE_NAME', 'mo_ear_test'),
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 国际化语言支持
LANGUAGES = (
    ('en', gettext_noop('English')),
    ('zh-hans', gettext_noop('Simplified Chinese')),
)
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(RUNTIME_DIR, 'static')


# 静态站点生成器
SITE_PAGES_DIR = utils.mkdirp(os.path.join(
    BASE_DIR, 'templates', 'pages'))


# 模板消息Tags名称重定义
MESSAGE_TAGS = {
    messages.DEBUG: 'dark',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}


# 设置日期时间显示格式
DATETIME_FORMAT = 'Y/m/d H:i:s'


# Django Admin
DJANGO_ADMIN_URL = _get_config('DJANGO_ADMIN_URL')


# Email
EMAIL_HOST = _get_config('EMAIL_HOST', '')
EMAIL_PORT = _get_config_int('EMAIL_PORT', 0)
EMAIL_HOST_USER = _get_config('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = _get_config('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_SSL = _get_config_bool('EMAIL_USE_SSL', True)
EMAIL_SUBJECT_PREFIX = '[MoEar] '
EMAIL_TIME_LIMIT = _get_config_int('EMAIL_TIME_LIMIT', 30)

DEFAULT_FROM_EMAIL = _get_config('DEFAULT_FROM_EMAIL', '')


# django-allauth
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_ADAPTER = 'core.adapters.AccountAdapter'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_ACTIVATION_DAYS = 7
ACCOUNT_USERNAME_MIN_LENGTH = 5
ACCOUNT_FORMS = {}
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_AUTO_SIGNUP = False


# Django-rest-framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}
if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append(
        'rest_framework.renderers.BrowsableAPIRenderer')


# Celeryd
CELERY_BROKER_URL = _get_config(
    'CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = _get_config(
    'CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')

CELERY_APP = 'server'
CELERY_TASK_TIME_LIMIT = 1800
CELERY_WORKER_CONCURRENCY = _get_config_int(
    'CELERY_WORKER_CONCURRENCY', 10)
CELERY_WORKER_PREFETCH_MULTIPLIER = _get_config_int(
    'CELERY_WORKER_PREFETCH_MULTIPLIER', 5)

CELERY_CREATE_DIRS = []
CELERY_WORKER_LOG_PATH = os.path.dirname(_get_config(
    'CELERY_WORKER_LOG_FILE',
    os.path.join(RUNTIME_DIR, 'log', 'celery', '%n%I.log')))
CELERY_CREATE_DIRS.append(CELERY_WORKER_LOG_PATH)

_default_exchange = Exchange('default', type='direct')
_email_exchange = Exchange('email', type='topic')
_crawl_exchange = Exchange('crawl', type='topic')

CELERY_TASK_QUEUES = {
    Queue('default', _default_exchange, routing_key='default'),
    Queue('email', _email_exchange, routing_key='email.#'),
    Queue('crawl', _crawl_exchange, routing_key='crawl.#'),
}
CELERY_TASK_DEFAULT_QUEUE = 'default'
CELERY_TASK_DEFAULT_EXCHANGE = 'default'
CELERY_TASK_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_TASK_DEFAULT_ROUTING_KEY = 'default'

CELERY_TASK_ROUTES = {
    'core.tasks.periodic_chain_crawl_package_deliver': {
        'queue': 'default',
        'routing_key': 'default',
    },
    'core.tasks.account_send_email_task': {
        'queue': 'email',
        'routing_key': 'email.account_mgr',
    },
    'deliver.tasks.deliver_book_task': {
        'queue': 'email',
        'routing_key': 'email.deliver_book',
    },
    'posts.tasks.package_post': {
        'queue': 'crawl',
        'routing_key': 'crawl.package',
    },
    'spiders.tasks.spider_post': {
        'queue': 'crawl',
        'routing_key': 'crawl.spider',
    },
}


# celerybeat
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

CELERY_BEAT_LOG_PATH = os.path.dirname(_get_config(
    'CELERY_BEAT_LOG_FILE',
    os.path.join(RUNTIME_DIR, 'log', 'celery', 'celeryd.log')))
CELERY_CREATE_DIRS.append(CELERY_BEAT_LOG_PATH)

# 书籍打包输出根路径
BOOK_PACKAGE_ROOT = utils.mkdirp(os.path.join(RUNTIME_DIR, 'books'))

if not PRODUCTION:
    for path in CELERY_CREATE_DIRS:
        if not os.path.exists(path):
            os.makedirs(path)


# Logging Settings
# https://docs.djangoproject.com/en/2.0/topics/logging/
LOGS_ROOT = os.path.join(RUNTIME_DIR, 'log', 'app')
if not os.path.exists(LOGS_ROOT):
    os.makedirs(LOGS_ROOT)
LOG_FORMAT = "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s"
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': LOG_FORMAT,
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'exceptionlog': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_ROOT, "exceptions.log"),
            'formatter': 'standard',
        },
        'errorlog': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_ROOT, "error.log"),
            'formatter': 'standard',
        },
        'postcommit': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_ROOT, "postcommit.log"),
            'formatter': 'standard',
        },
        'middleware': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_ROOT, "middleware.log"),
            'formatter': 'standard',
        },
        'db': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_ROOT, "db.log"),
            'formatter': 'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'restapi': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_ROOT, "api.log"),
            'formatter': 'standard',
        },
        'core': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_ROOT, "core.log"),
            'formatter': 'standard',
        },
        'pages': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_ROOT, "pages.log"),
            'formatter': 'standard',
        },
        'posts': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_ROOT, "posts.log"),
            'formatter': 'standard',
        },
        'spiders': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_ROOT, 'spiders.log'),
            'formatter': 'standard',
        },
        'deliver': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_ROOT, 'deliver.log'),
            'formatter': 'standard',
        },
        'console': {
            'level': ('INFO', 'DEBUG')[DEBUG],
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['errorlog'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['db'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['exceptionlog'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'core.views.post_commit': {
            'handlers': ['postcommit'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'core.middleware': {
            'handlers': ['middleware'],
            'level': 'DEBUG',
            'propagate': False,
        },

        # 应用中的模型日志
        'restapi': {
            'handlers': ['restapi', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'core': {
            'handlers': ['core', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'pages': {
            'handlers': ['pages', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'posts': {
            'handlers': ['posts', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'spiders': {
            'handlers': ['spiders', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'deliver': {
            'handlers': ['deliver', 'console'],
            'level': 'INFO',
            'propagate': False,
        },

        # Default handler for everything that we're doing. Hopefully this
        # doesn't double-print the Django things as well. Not 100% sure how
        # logging works :)
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
