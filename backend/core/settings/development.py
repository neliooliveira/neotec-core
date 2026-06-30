import os
from core.settings.base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

# Database
DATABASES['default']['NAME'] = 'neotec_core_dev'

# CORS - Allow all in development
CORS_ALLOW_ALL_ORIGINS = True

# Email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
