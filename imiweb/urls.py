from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^imiweb/', include('imiweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    (r'imictl/get/infrastructures', 'imiservicer.views.getInfrastructures'),
    (r'imictl/get/entities', 'imiservicer.views.getEntities'),
    (r'imictl/get/products', 'imiservicer.views.getProducts'),
    (r'imictl/frm/entities', 'imiservicer.views.entitiesForm'),
    
    # Templates for dojo
    (r'^tpl/header', 'django.views.generic.simple.direct_to_template',{'template': 'dojo/header.django.html'}),
    
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    
    (r'^$', 'django.views.generic.simple.direct_to_template',{'template': 'base.django.html'}),
)

# If we are developing let the Django test server handle static files
from django.conf import settings
if getattr(settings, 'LOCAL_DEV', True):
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',   
            {'document_root':settings.MEDIA_ROOT}),
    )