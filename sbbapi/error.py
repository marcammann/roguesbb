class MissingParameter(Exception):
	def __init__(self, value):
		self.param_name = value
			
	def __str__(self):
		return 'Missing Parameter: {param_name}'.format(param_name=self.param_name)
		
		
class SBBRequestError(Exception):
	def __init__(self, value):
		self.response = value
		
	def __str__(self):
		return 'Generic SBB Request Error: Code: {status}'.format(self.response['status'])
		
		
class NotYetImplemented(Exception):
	def __init__(self):
		pass
		
	def __str__(self):
		return 'This method has yet to come, but help is always welcome!'