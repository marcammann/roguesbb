
class RequestHandler:
    def __init__(self):
        pass

    def check(self):
        pass
        
    def build(self, object, method, parameters[]):
        paramstr = ''
        
        for key, value in parameters:
            paramstr += '%s=%s&' % key, value
        
        self.request = '%s.%s?%s' % object, method, paramsstr
        
        return true