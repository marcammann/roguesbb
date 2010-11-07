import pprint

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from searchform.controllers.SBBApi import SBBApi
from searchform.controllers.RequestHandler import RequestHandler
from searchform.controllers.ResponseHandler import ResponseStationHandler

class StationsHandler:
    def __init__(self, request):                
        station_query = request.GET.get('q', '')
        
        req = RequestHandler('stations', 'getFromString', {'station_query':station_query})
        
        sbbapi = SBBApi()
        sbbapi.open()
        response = ResponseStationHandler(sbbapi.request(req))
        
        if response.check():
            self.response = response.get()
            pprint.pprint(response.get())
            
        else:
            self.response = '<b>The request failed</b>'
        
    def render(self, themepath):
        return render_to_response(themepath, {
                'response': self.response
            }
        )