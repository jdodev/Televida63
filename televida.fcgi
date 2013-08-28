#!/home5/dbriones/python/bin/python
import sys, os

# Where /home/your_username is the path to your home directory
sys.path.insert(0, "/home5/dbriones/python")
sys.path.insert(13, "/home5/dbriones/django-projects/televida")

os.environ['DJANGO_SETTINGS_MODULE'] = 'televida.settings'
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
