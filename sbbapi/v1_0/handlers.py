from piston.handler import BaseHandler
from piston.utils import rc

from piston.handler import BaseHandler
from sbbapi.v1_0.controllers.schedules import SchedulesController
from sbbapi.v1_0.controllers.stations import StationsController

#from sbbapi.error import PaginationError, TagNotFoundError, EventNotFoundError, MissingIdError

import sys, types

controllers = ('schedules', 'stations')

class ApiHandler(BaseHandler):
	def read(self, request, method_name, entity_name, is_private = False):
		def str_to_class(field):
			try:
				identifier = getattr(sys.modules[__name__], field)
			except AttributeError:
				raise NameError("%s doesn't exist." % field)
			if isinstance(identifier, (types.ClassType, types.TypeType)):
				return identifier
			raise TypeError("%s is not a class." % field)
			
		if entity_name in controllers:
			class_name = entity_name[:1].upper() + entity_name[1:] + 'Controller'
			controller = str_to_class(class_name)
			
			c = controller()
			if not hasattr(c, method_name):
				return rc.NOT_FOUND
			method = getattr(c, method_name)
			
			#print repr(method)
			
			#print repr(method.private)
			
			if hasattr(method, 'private') and method.private != is_private:
				raise Exception('Not authorized')
			
			if hasattr(method, 'request_methods') and 'GET' not in method.request_methods:
				raise Exception('Invalid Request Method, use %s' % repr(method.request_methods) ) 
			
			try:
				retval = method(request=request)
				
				return retval
			#except (PaginationError, TagNotFoundError, EventNotFoundError):
			#	return rc.NOT_FOUND
			except Exception,e :
				#print repr(e)
				raise e
		else:
			return rc.NOT_FOUND
		

class PrivateApiHandler(ApiHandler):
	def read(self, request, method_name, entity_name, is_private = True):
		return super(PrivateApiHandler, self).read(request = request, 
			method_name = method_name, entity_name = entity_name, 
			is_private = is_private)
