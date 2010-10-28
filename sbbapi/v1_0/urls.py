from django.conf.urls.defaults import *
from piston.resource import Resource
from sbbapi.v1_0.handlers import ApiHandler

api_handler = Resource(ApiHandler)

urlpatterns = patterns('',
	url(r'(?P<entity_name>[^.^/]+)\.(?P<method_name>[^.^/]+)', api_handler),
)