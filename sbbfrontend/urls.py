from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^searchform/', include('sbbfrontend.searchform.urls')),
    
    (r'^sitemedia/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/Users/peter/projects/sbb/repos/roguesbb/sbbfrontend/media'}),
)