"""
WSGI config for tutorial project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""


import os
from django.core.wsgi import get_wsgi_application
#from whitenoise.djangyo import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.tutorial.settings")

application = get_wsgi_application()
#application = DjangoWhiteNoise(application)
