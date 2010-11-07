import pprint
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

import time;
from datetime import datetime

from searchform.models import Searchform
from searchform.controllers.SBBApi import SBBApi
from searchform.controllers.RequestHandler import RequestHandler
from searchform.controllers.ResponseHandler import ResponseConnectionHandler

class SchedulesHandler:
    def __init__(self, request):
        self.request = request
        
        if self.request.method == 'POST':
            self.form = Searchform(request.POST)
            
            if self.form.is_valid():
                # get schedules from api

                
                departure_id=self.request.POST.get('id_station_from_station_id',0)
                arrival_id=self.request.POST.get('id_station_to_station_id',0)
                is_arrival_time=False
                fdate = self.form.cleaned_data['date']
                ftime = self.form.cleaned_data['time']
                ftimestamp = time.mktime(datetime.combine(fdate, ftime).timetuple())
                
                if departure_id is None or arrival_id is None or departure_id == 0 or arrival_id == 0:
                    # TODO: error handling
                    return False
                
                if fdate is None or ftime is None:
                    # TODO: error handling
                    return False
                
                params = {}
                params['departure_id'] = departure_id
                params['arrival_id'] = arrival_id
                if is_arrival_time:
                    params['arrival_time'] = ftimestamp
                else:
                    params['departure_time'] = ftimestamp
                
                pprint.pprint(params)
                
                #req = RequestHandler('schedules', 'query', {'departure_id': departure_id, 'arrival_id': arrival_id, 'is_arrival_time': is_arrival_time, 'date': date, 'time':time})
                #req = RequestHandler('schedules', 'query', {'departure_id': departure_id, 'arrival_id': arrival_id})
                req = RequestHandler('schedules', 'query', params) 
                
                
                sbbapi = SBBApi()
                sbbapi.open()
                response = ResponseConnectionHandler(sbbapi.request(req))
                
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