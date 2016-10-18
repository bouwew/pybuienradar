import pybuienradar
import time

now = time.strftime("%H:%M")
timeframe = 3600
latitude = '52.151682'
longitude = '6.064496'

buienradar = pybuienradar.forecast(latitude, longitude)
forecast_data = buienradar.get_forecast_data()
forecast = buienradar.get_forecast(now,timeframe)

print (forecast_data)
print (forecast)

print (forecast['averagerain'])
print (forecast['totalrain'])
