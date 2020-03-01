"""
WSGI config for Django_Demo_Blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Demo_Blog.settings')
sys.path.append('~/.pyenv/versions/3.7.5/lib/python3.7/site-packages')
application = get_wsgi_application()
