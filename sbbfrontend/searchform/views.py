from datetime import date, datetime


from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from searchform.models import Request, Searchform

def form(request):
    arequest = Request()
    connections = arequest.getConnections()
    today = date.today().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M")
    
    return render_to_response('searchform/index.html', {
        'connections': connections,
        'today': today,
        'time' : time
    }, context_instance=RequestContext(request))

def searchform(request):
    result = ''
    
    if request.method == 'POST':
        form = Searchform(request.POST)
        if form.is_valid():
            results = 'yay'
            # Get connections via API
    else:
        form = Searchform()
        
    return render_to_response('searchform/searchform.html', {
        'form': form,
        'results': result
    })