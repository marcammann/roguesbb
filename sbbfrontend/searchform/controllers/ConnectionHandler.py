import urllib2
import json as simplejson

class ConnectionException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)

class ConnectionHandler:
    def __init__(self):
        pass

    def open(self):
        pass