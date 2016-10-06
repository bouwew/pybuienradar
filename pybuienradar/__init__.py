from urllib.request import urlopen
from datetime import datetime
from datetime import timedelta
import time

class buienradar():
    pass

class rainprediction(buienradar):
    def __init__ (self, latitude, longitude):
        self._latitude = latitude
        self._longitude = longitude
    def getprediction(self):
        '''
        This will get the list with rain predictions for a GPS location and transform them into a python dictionary
        Instantiate the class with gps latitude and longitude in decimal degrees notation
        '''
        url = "http://gadgets.buienradar.nl/data/raintext?lat=%s&lon=%s"
        response = urlopen(url % (self._latitude, self._longitude)).read().decode()
        prediction = {}
        for line in response.splitlines():
            (val,key) = line.split("|")
            prediction[(key)] = val
        return (prediction)
    def calculatetotalandaverage(self, offset):
        '''
        This will calculate the total and average rainfall for the given timeframe (now + offset)
        Averages are per 5 minutes within the timeframe
        0 is no rain, 255 is very heavy rain
        -- When needed, mm/h can be calculated by 10^((value -109)/32) (example: 77 = 0.1 mm/hour)
        '''
        willitrain = self.getprediction()
        now = time.strftime("%H:%M")
        int_totalrain = 0
        int_averagerain = 0
        int_numberoflines = 0
        for key in willitrain:
            tdelta = datetime.strptime(key, '%H:%M') - datetime.strptime(now, '%H:%M')
            if tdelta.days < 0:
                tdelta = timedelta(days=0,seconds=tdelta.seconds, microseconds=tdelta.microseconds)
            if tdelta.seconds > 0 and tdelta.seconds <= offset:
                int_totalrain = int_totalrain + int(willitrain[key])
                int_numberoflines = int_numberoflines + 1
                int_averagerain = int_totalrain / int_numberoflines
        return ({'time': now, 'offset': offset, 'totalrain': int_totalrain, 'averagerain': int_averagerain})
