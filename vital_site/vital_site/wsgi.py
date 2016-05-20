"""
WSGI config for vital_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))
sys.path.append(PROJECT_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vital_site.settings")

from django.core.wsgi import get_wsgi_application
_application = get_wsgi_application()