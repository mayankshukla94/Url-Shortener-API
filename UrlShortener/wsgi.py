"""
WSGI config for UrlShortener project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from decouple import config
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

if config('DJANGO_DEVELOPMENT') == 'dev':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UrlShortener.settings.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UrlShortener.settings.settings')

application = get_wsgi_application()
application = WhiteNoise(application)