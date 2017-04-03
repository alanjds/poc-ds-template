"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_wsgi_application()

# Whitenoise: https://pypi.python.org/pypi/whitenoise
# Serve static assets in a "safe" way on herokuish environments
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
