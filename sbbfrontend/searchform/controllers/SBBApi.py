from searchform.controllers.SBBApi import SBBApi

class SBBApiError(Exception):
    pass
    
class SBBApi(Connection):
    def __init__(self):
        pass
        
    def call(self, request):
        url = self.base_url+request.
        
        try:
            result = simplejson.load(urllib2.urlopen(url))
        except:
            raise Exception('Something went wrong!')

        return result