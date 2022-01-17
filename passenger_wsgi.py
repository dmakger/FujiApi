import os, sys
sys.path.insert(0, '/home/s/dmakger.beget.tech/fuji')
sys.path.insert(1, '/home/s/dmakger.beget.tech/djangoenv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'fuji.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()