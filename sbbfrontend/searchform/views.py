from datetime import date, datetime


from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from searchform.models import Searchform
from searchform.controllers.api import SBBApi

def searchform(request):
    connections = ''
    
    if request.method == 'POST':
        form = Searchform(request.POST)
        if form.is_valid():
            # Get connections via API
            sbbapi = SBBApi('')
            connections = sbbapi.getConnections(form.cleaned_data['station_from'])

    else:
        form = Searchform()
    
    return render_to_response('searchform/form.html', {
            'form': form,
            'connections': connections
        }, context_instance=RequestContext(request)
    )