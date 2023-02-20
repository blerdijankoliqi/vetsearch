from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bf*ydng!hw3c_f_4a1s%(eq_gt0val95*pdev2i7&2ek15(@ft'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['kolic.me', 'www.kolic.me', 'localhost', '127.0.0.1'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
