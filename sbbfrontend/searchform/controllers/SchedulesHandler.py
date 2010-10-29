from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from searchform.models import Searchform
from searchform.controllers.SBBApi import SBBApi

class SchedulesHandler:
    def __init__(self, request):
        self.request = request
        
        if self.request.method == 'POST':
            self.form = Searchform(request.POST)
            if self.form.is_valid():
                # get schedules from api
                
                departure_id='008503011'#form.cleaned_data['station_from']
                arrival_id='008506000'#form.cleaned_data['station_to']
                is_arrival_time=0#form.cleaned_data['isat']
                date='20101031'#form.cleaned_data['date']
                time='0900'#form.cleaned_data['time']
                request = Request('schedules', 'query', {'departure_id':departure_id, 'arrival_id':departure_id, 'is_arrival_time'=is_arrival_time, 'date'=date, 'time'=time})

                sbbapi = SBBApi
                self.response = Response(sbbapi.open(request))
                
                #form.cleaned_data['station_from']
                
                connections = response.get('json')
                
        else:
            form = Searchform()
    
    def render(self, themepath):
        return render_to_response(themepath, {
                'form': self.form,
                'response': self.response
            }, context_instance=RequestContext(self.request)
        )