from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
   # all my other url mappings
   (r'^sbb/1.0', include('sbbapi.v1_0.urls')),
)
