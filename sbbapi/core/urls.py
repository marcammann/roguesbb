from django.conf.urls.defaults import *
from piston.resource import Resource
from sbbapi.core.handlers import SchedulesHandler, StationsHandler, StationHandler, LineHandler, ConnectionHandler

schedules_handler = Resource(SchedulesHandler)
stations_handler = Resource(StationsHandler)
station_handler = Resource(StationHandler)
line_handler = Resource(LineHandler)
connection_handler = Resource(ConnectionHandler)

urlpatterns = patterns('',
	url(r'(?P<entity_name>)\.(?P<method_name>)', schedules_handler),
	url(r'(?P<entity_name>)\.(?P<method_name>)', stations_handler),
	url(r'(?P<entity_name>)\.(?P<method_name>)', station_handler),
	url(r'(?P<entity_name>)\.(?P<method_name>)', line_handler),
	url(r'(?P<entity_name>)\.(?P<method_name>)', connection_handler)
)