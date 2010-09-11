from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'searchform.views.form', name="home"),
    url(r'^searchform$', 'searchform.views.searchform', name="blah"),
    
    (r'^sitemedia/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/Users/peter/projects/sbb/repos/roguesbb/frontend/media'}),
            
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
