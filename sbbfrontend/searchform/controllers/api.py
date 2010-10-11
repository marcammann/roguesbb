import urllib2
import json as simplejson
    
class SBBApiError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)

class SBBApi:
    def __init__(self, api_key):
            self.base_url = 'http://openlibrary.org/authors/' + api_key
    
    def checkResponse(self, resp):
        if resp["name"]:
            return resp
        else:
            raise SBBApiError('Something went wrong!')
            
    def getConnections(self, name='OL1A'):
        url = self.base_url+name+'.json'
        try:
            result = simplejson.load(urllib2.urlopen(url))
        except:
            raise Exception('Something went wrong!')

        return self.checkResponse(result)
        #return ['12:01', '13:01', '13:30']