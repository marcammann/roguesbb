from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from searchform.controllers.SBBApi import SBBApi

class StationsHandler:
    def __init__(self):                
        station_query='Appenz'#parameter
        
        #stations.getFromString?station_query=Winterthur
        request = Request('stations', 'getFromString', {'station_query':station_query})

        sbbapi = SBBApi
        response = Response(sbbapi.open(request))
        
        self.response = response.get
        
    def render(self, themepath):
        return render_to_response(themepath, {
                'response': self.response
            }, context_instance=RequestContext(self.request)
        )