"""
WSGI config for QuoteApplication project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
# path = '/PATH/TO/PROJECT'
# if (path not in sys.path):
#     sys.path.append(path)
#
# sys.path.append('PATH/TO/VENV/PACKAGES')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QuoteApplication.settings')

application = get_wsgi_application()
