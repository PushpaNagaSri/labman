"""
WSGI config for labman project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import sys
import os
from django.core.wsgi import get_wsgi_application

sys.path.append(os.path.join(os.path.dirname(__file__), 'labman'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'labman.settings')

application = get_wsgi_application()
