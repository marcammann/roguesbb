import json as simplejson

class ResponseHandler:
    def __init__(self, resp):
        self.response = resp

    def check(self, resp):
        if resp['request_id']:
            return true
        else:
            return false
            
    def get(self):
        return self.response