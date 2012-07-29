import os
import sys

root_dir = "/srv/www/lapinlabs.com"
proj_name = "imiweb"

sys.path.append(root_dir + "/_siteenv/lib/python2.7/site-packages")
sys.path.append(root_dir)
sys.path.append(root_dir + "/" + proj_name)
sys.path.append(root_dir + "/imistate")
sys.path.append(root_dir + "/imicommander")
sys.path.append(root_dir + "/imiservicer")

os.environ['DJANGO_SETTINGS_MODULE'] = 'imiweb.settings'

import django.core.handlers.wsgi 
application = django.core.handlers.wsgi.WSGIHandler()
