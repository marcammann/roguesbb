from searchform.controllers.SchedulesHandler import SchedulesHandler

#searchform (with response)
def searchform(request):
    schedules = SchedulesHandler(request)
    return schedules.render('searchform/form.html')
    
def getStations(request):
    stations = StationsHandler
    return schedules.render('searchform/stations.html')