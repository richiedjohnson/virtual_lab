"""
WSGI config for vital_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

def application(environ, start_response):
    _application = get_wsgi_application()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vital_site.settings")
    os.environ.setdefault("VITAL_DB_NAME", environ['VITAL_DB_NAME'])
    os.environ.setdefault("VITAL_DB_HOST", environ['VITAL_DB_HOST'])
    os.environ.setdefault("VITAL_DB_PORT", environ['VITAL_DB_PORT'])
    os.environ.setdefault("VITAL_DB_USER", environ['VITAL_DB_USER'])
    os.environ.setdefault("VITAL_DB_PWD", environ['VITAL_DB_PWD'])
    os.environ.setdefault("VITAL_EMAIL_HOST", environ['VITAL_EMAIL_HOST'])
    os.environ.setdefault("VITAL_EMAIL_PORT", environ['VITAL_EMAIL_PORT'])
    os.environ.setdefault("VITAL_EMAIL_USER", environ['VITAL_EMAIL_USER'])
    os.environ.setdefault("VITAL_EMAIL_PWD", environ['VITAL_EMAIL_PWD'])
    return _application(environ, start_response)