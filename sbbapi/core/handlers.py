from piston.handler import BaseHandler
from sbbapi.core.controllers.schedules import SchedulesController




class ApiHandler(BaseHandler):
	def read(self, request, method_name, entity_name):
		c = SchedulesController()
		c.get(request=request)
		
		
	
class SchedulesHandler(ApiHandler):
	pass
	
class StationsHandler(ApiHandler):
	pass
	
class StationHandler(ApiHandler):
	pass
	
class LineHandler(ApiHandler):
	pass
	
class ConnectionHandler(ApiHandler):
	pass
	