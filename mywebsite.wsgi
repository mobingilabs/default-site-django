import os
import sys	
sys.path.append('/srv/django/app/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mywebsite.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
