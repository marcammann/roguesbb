from django.db import models
from django import forms

class Searchform(forms.Form):
    station_from = forms.CharField(max_length=50,required=True)
    station_to = forms.CharField(max_length=50,required=True)
    station_via = forms.CharField(max_length=50,required=False)
    date = forms.DateField(required=True)
    time = forms.DateField(required=True)
    isat = forms.CheckBox(value=True)
    
class Station(models.Model):
    station_id = models.IntegerField()
    station_name = models.CharField(max_length=100)
    station_coordinate = models.CharField(max_length=100)
    station_size = models.CharField(max_length=100)
    
    def getInfo(self, station_id):
        return ''

class Fragment(models.Model):
    departure_station = models.ForeignKey(Station, related_name="frag_departure_station")
    arrival_station = models.ForeignKey(Station, related_name="frag_arrival_station")
    departure_time = models.DateField()
    arrival_time = models.DateField()
    departure_platform = models.CharField(max_length=5)
    arrival_platform = models.CharField(max_length=5)

class Connection(models.Model):
    connection_id = models.IntegerField()
    departure_station = models.ForeignKey(Station, related_name="conn_departure_station")
    arrival_station = models.ForeignKey(Station, related_name="conn_arrival_station")
    fragment = models.ForeignKey(Fragment)
    
    def getInterruption(self, connection_id):
        return ''

class Schedule(models.Model):
    request_id = models.IntegerField()
    connections = models.ForeignKey(Connection)
    
    def get(self):
        return ''
        
    def getLater(self, schedules_request_id):
        return ''
        
    def getEarlier(self, schedules_request_id):
        return ''
        

class Stations(models.Model):
    def getFromString(self):
        return ''

    def getFromCoordinate(self):
        return ''

class Line(models.Model):
    type = models.CharField(max_length=100)
    headsign = models.CharField(max_length=100)
    operator = models.CharField(max_length=100)

    def getInfo(self, line_id):
        return ''
