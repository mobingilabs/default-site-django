
import os
import sys	
sys.path.append('/srv/django/app/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mywebsite.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
