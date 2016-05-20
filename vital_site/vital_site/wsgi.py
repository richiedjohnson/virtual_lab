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


def application(environ, start_response):
    print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>IN APPLICATION>>>>>>>>>>>>>>>"
    print "<>", environ['VITAL_DB_NAME'], "<>"
    os.environ.setdefault("VITAL_DB_NAME", environ['VITAL_DB_NAME'])
    os.environ.setdefault("VITAL_DB_HOST", environ['VITAL_DB_HOST'])
    os.environ.setdefault("VITAL_DB_PORT", environ['VITAL_DB_PORT'])
    os.environ.setdefault("VITAL_DB_USER", environ['VITAL_DB_USER'])
    os.environ.setdefault("VITAL_DB_PWD", environ['VITAL_DB_PWD'])
    os.environ.setdefault("VITAL_EMAIL_HOST", environ['VITAL_EMAIL_HOST'])
    os.environ.setdefault("VITAL_EMAIL_PORT", environ['VITAL_EMAIL_PORT'])
    os.environ.setdefault("VITAL_EMAIL_USER", environ['VITAL_EMAIL_USER'])
    os.environ.setdefault("VITAL_EMAIL_PWD", environ['VITAL_EMAIL_PWD'])
    print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>OUT APPLICATION>>>>>>>>>>>>>>>"
    return _application(environ, start_response)