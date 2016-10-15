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
        This will get the list with rain predictions for a GPS location and transform them into a python dictionary
        Instantiate the class with gps latitude and longitude in decimal degrees notation
        '''
        data = urlopen(self._url % (self._latitude, self._longitude)).read().decode()
        forecast = {}
        for line in data.splitlines():
            (val,key) = line.split("|")
            forecast[(key)] = val
        return (forecast)
    def get_forecast(self, now, timeframe):
        '''
        This will return the total and average rainfall for the given timefram (now + timeframe)
        Averages are per 5 minutes within the timeframe
        0 is no rain, 255 is very heavy rain
        -- When needed, mm/h can be calculated by 10^((value -109)/32) (example: 77 = 0.1 mm/hour)
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
                totalrain = totalrain + int(data[key])
                numberoflines = numberoflines + 1
                averagerain = totalrain / numberoflines
        return ({'time': now, 'timeframe': timeframe, 'totalrain': totalrain, 'averagerain': averagerain})
