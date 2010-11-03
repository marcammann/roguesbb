import json

class ResponseHandler:
    def __init__(self, resp):
        self.response = resp['response']
        self.content = resp['content']

    def check(self):
        if self.response['status'] == '200':
            return True
        else:
            return False
            
    def get(self):
        resp = json.loads(self.content)
        return resp['connections']