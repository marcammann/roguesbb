from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'', 'searchform.views.searchform'),
    url(r'stations/get/$1', 'searchform.views.stations'),
)