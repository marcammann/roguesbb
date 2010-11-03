import json
import pprint

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

from datetime import datetime

from searchform.models import Searchform
from searchform.controllers.SBBApi import SBBApi
#from searchform.controllers.ConnectionHandler import ConnectionHandler
from searchform.controllers.RequestHandler import RequestHandler
from searchform.controllers.ResponseHandler import ResponseHandler

class SchedulesHandler:
    def __init__(self, request):
        self.request = request
        
        if self.request.method == 'POST':
            self.form = Searchform(request.POST)
            
            if self.form.is_valid():
                # get schedules from api
                departure_id='008503011' #form.cleaned_data['station_from']
                arrival_id='008506000' #form.cleaned_data['station_to']
                is_arrival_time=0 #form.cleaned_data['isat']
                date='20101031' #form.cleaned_data['date']
                time='0900' #form.cleaned_data['time']
                
                if departure_id is None or arrival_id is None:
                    # TODO: error handling
                    return False
                
                if date is None:
                    date = datetime.now()
                if time is None:             
                    time = datetime.now()
                
                
                #req = RequestHandler('schedules', 'query', {'departure_id': departure_id, 'arrival_id': arrival_id, 'is_arrival_time': is_arrival_time, 'date': date, 'time':time})
                req = RequestHandler('schedules', 'query', {'departure_id': departure_id, 'arrival_id': arrival_id})
                
                sbbapi = SBBApi()
                sbbapi.open()
                response = ResponseHandler(sbbapi.request(req))
                
                if response.check():
                    self.response = response.get()
                    
                else:
                    self.response = '<b>The request failed</b>'
                
            else:
                self.response = '<b>The form values aren\'t valid</b>'
                
        else:
            self.form = Searchform()
            self.response = None
        
    def render(self, themepath):
        return render_to_response(themepath, {
                'form': self.form,
                'response': self.response
            }, context_instance=RequestContext(self.request)
        )