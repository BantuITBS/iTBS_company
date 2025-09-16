import os
import sys

path = '/home/Takawira/iTBS_project'

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'iTBS_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()