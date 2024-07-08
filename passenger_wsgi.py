import os
import sys

PROJECT_DIR = '/home/app1saen/public_html/socialpost'
sys.path.insert(0, PROJECT_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'socialpost.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
