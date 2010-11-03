
class RequestHandler:
            
    def __init__(self, object, method, parameters):
        paramstr = ''
        
        for value in parameters:
            paramstr += '%s=%s&' % (value, parameters[value])
        
        self.uri = '%s.%s?%s' % (object, method, paramstr)