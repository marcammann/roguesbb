from django.db import models

class schedule(models.Model):
    request_id = models.IntegerField()
    connections = models.ForeignKey(connection)
    
    def get():
        return ''
        
    def getLater(schedules_request_id):
        return ''
        
    def getEarlier(schedules_request_id):
        return ''
        

class stations(models.Model):
    def getFromString():
        return ''

    def getFromCoordinate():
        return ''

class station(models.Model):
    station_id = models.IntegerField()
    station_name = models.CharField(max_length=100)
    station_coordinate = models.CharField(max_length=100)
    station_size = models.CharField(max_length=100)
    
    def getInfo(station_id):
        return ''


class line(models.Model):
    def getInfo(line_id):
        return ''

class connection(models.Model):
    connection_id = models.IntegerField()
    departure_station = models.ForeignKey(station)
    arrival_station = models.ForeignKey(station)
    connections = models.ForeignKey(fragment)
    
    def getInterruption(connection_id):
        return ''

class fragment(models.Model):
    departure_station = models.ForeignKey(station)
    arrival_station = models.ForeignKey(station)
    departure_time = models.DateField()
    arrival_time = models.DateField()
    departure_platform = models.CharField(max_length=5)
    arrival_platform = models.CharField(max_length=5)
    connections = models.ForeignKey(line)
    
class line(models.Model):
    type = models.CharField(max_length=100)
    headsign = models.CharField(max_length=100)
    operator = models.CharField(max_length=100)
