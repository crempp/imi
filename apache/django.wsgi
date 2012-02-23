import os, sys

# path is the parent directory of this script ('/var/www' in this case)
#path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# we check for path because we're told to at the tail end of
# http://code.google.com/p/modwsgi/wiki/ConfigurationDirectives#WSGIReloadMechanism 
#if path not in sys.path:
#    sys.path.append(path)

sys.path.append('/web/imi.chadrempp.com')
sys.path.append('/web/imi.chadrempp.com/imiweb')
sys.path.append('/web/imi.chadrempp.com/imistate')
sys.path.append('/web/imi.chadrempp.com/imicommander')
sys.path.append('/web/imi.chadrempp.com/imiservicer')

os.environ['DJANGO_SETTINGS_MODULE'] = 'imiweb.settings'

# Fixes Improperly configured error
# See http://groups.google.com/group/django-feincms/msg/68ff5462061fa84b
#from django.core.management.validation import get_validation_errors 
#try: 
#        from cStringIO import StringIO 
#except ImportError: 
#        from StringIO import StringIO 
#s = StringIO() 
#num_errors = get_validation_errors(s, None) 
import django.core.handlers.wsgi 
application = django.core.handlers.wsgi.WSGIHandler()