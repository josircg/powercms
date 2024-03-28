# -*- coding: utf-8 -*-
from .settings import *

DEBUG = True

for template_config in TEMPLATES:
    template_config['OPTIONS']['debug'] = DEBUG

SITE_NAME = '%(titulo)s'
SITE_HOST = 'http://%(host)s'

# python -c "import secrets; print(secrets.token_urlsafe())"
SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '%(dbname)s',
        'USER': '%(dbuser)s',
        'PASSWORD': '%(dbpassword)s',
        'HOST': '%(dbhost)s',
        'PORT': '',
    },
}

ALLOWED_HOSTS = ['%(host)s', 'www.%(host)s', ]

ADMINS= (('IRDX', 'josircg@gmail.com'),)
SERVER_EMAIL='%(from)s'
REPLY_TO_EMAIL='%(from)s'
DEFAULT_FROM_EMAIL='%(from)s'

LOGOUT_REDIRECT_URL = '/admin/login'

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error', ]
NOCAPTCHA = True
RECAPTCHA_USE_SSL = True

RECAPTCHA_DOMAIN = 'www.recaptcha.net'
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
SITEMAP = 'Home'  # Home ou All
