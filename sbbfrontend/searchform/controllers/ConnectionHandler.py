#from httplib2 import Http
import httplib2

DEFAULT_TIMEOUT=10 #seconds
HOST='http://91.192.100.62:8001/sbb/1.0/'

class ConnectionHandler:
    def __init__(self, ssl=False, cache=None, timeout=DEFAULT_TIMEOUT, proxy_info=None):
        self.ssl = ssl
        self.cache = cache
        self.timeout = timeout
        self.proxy_info = proxy_info
        
    def open(self):
        self.http = httplib2.Http(self.cache, self.timeout, self.proxy_info)
        return True

    def request(self, request):
        #connection_type = HTTPSConnection if self.ssl else HTTPConnection
        print HOST+request.uri
        
        try:
            response, content = self.http.request(HOST+request.uri, "GET", None, None, httplib2.DEFAULT_MAX_REDIRECTS)#, connection_type)
        except Exception,e:
            raise ConnectionHandlerException(e, "Connection to API failed")
        
        return {
            'response':response,
            'content':content,
        }
        

class ConnectionHandlerException(Exception):
    def __init__(self, exception, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)
