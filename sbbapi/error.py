class MissingParameter(Exception):
	def __init__(self, value):
		self.param_name = value
			
	def __str__(self):
		return 'Missing Parameter: {param_name}'.format(param_name=self.param_name)