from urllib.request import urlopen
from datetime import datetime
from datetime import timedelta
import time

class buienradar():
    pass

class forecast(buienradar):
    def __init__ (self, latitude, longitude):
        self._latitude = latitude
        self._longitude = longitude
        self._url = "http://gadgets.buienradar.nl/data/raintext?lat=%s&lon=%s"
    def get_forecast_data(self):
        '''
        This will get the list with rain predictions in mm/h for a GPS location and transform them into a python dictionary
        Instantiate the class with gps latitude and longitude in decimal degrees notation
        '''
        data = urlopen(self._url % (self._latitude, self._longitude)).read().decode()
        forecast = {}
        for line in data.splitlines():
            (val,key) = line.split("|")
            mm = 10**((int(val) - 109)/32)
            forecast[(key)] = mm
        return (forecast)
    def get_forecast(self, now, timeframe):
        '''
        This will return the total and average rainfall in mm/h for the given timeframe (now + timeframe)
        '''
        data = self.get_forecast_data()
        totalrain = 0
        averagerain = 0
        numberoflines = 0
        for key in data:
            tdelta = datetime.strptime(key, '%H:%M') - datetime.strptime(now, '%H:%M')
            if tdelta.days < 0:
                tdelta = timedelta(days=0,seconds=tdelta.seconds, microseconds=tdelta.microseconds)
            if tdelta.seconds > 0 and tdelta.seconds <= timeframe:
                totalrain = totalrain + float(data[key])
                numberoflines = numberoflines + 1
                averagerain = round((totalrain / numberoflines),2)
        return ({'time': now, 'timeframe': timeframe, 'totalrain': round((totalrain),2), 'averagerain': averagerain})
