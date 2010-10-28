#from tedapi.error import MissingIdError

def requires_id(func):
	def _inner(self, request):
		if not request.GET.get('id', False):
			#raise MissingIdError
			return False
		else:
			return func(self=self, request=request)
			
	return _inner
	
	
def private(func):
	def _inner(self, request):
		return func(self=self, request=request)
		
	print repr('private called')
	_inner.private = True
	return _inner
	
	
def GET(func):
	def _inner(self, request):
		return func(self=self, request=request)
	
	request_methods = ['GET',]
	if hasattr(func, 'request_methods'):
		request_methods.extend(func.request_methods)
		
	_inner.request_methods = request_methods
	return _inner
	
	
def POST(func):
	def _inner(self, request):
		return func(self=self, request=request)

	request_methods = ['POST',]
	if hasattr(func, 'request_methods'):
		request_methods.extend(func.request_methods)

	_inner.request_methods = request_methods
	return _inner
	
		
class BaseController():
	pass
