from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'stations/get', 'searchform.views.stations'),
    url(r'', 'searchform.views.searchform'),
)