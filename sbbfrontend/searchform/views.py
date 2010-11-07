from searchform.controllers.SchedulesHandler import SchedulesHandler
from searchform.controllers.StationsHandler import StationsHandler

#searchform (with response)
def searchform(request):
    schedules = SchedulesHandler(request)
    return schedules.render('searchform/form.html')
    
def stations(request):
    stations = StationsHandler(request)
    return stations.render('searchform/stations.html')