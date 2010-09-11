class GET:
	def __init__(self, func):
		self.func = func
		
	def __call__(self, request, *args):
		print repr(args)
		print 'calling ', self.func.__name__
		

class SchedulesController:
	@GET
	def get(self, params):
		pass
		
	@GET
	def getLater(self, params):
		pass
	
	@GET
	def getEarlier(self, params):
		pass