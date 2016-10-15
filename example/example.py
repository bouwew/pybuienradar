import pybuienradar
import time

now = time.strftime("%H:%M")
timeframe = 3600
latitude = '52.0893191'
longitude = '5.110169100000007'

buienradar = pybuienradar.forecast(latitude, longitude)
forecast_data = buienradar.get_forecast_data()
forecast = buienradar.get_forecast(now,timeframe)

print (forecast_data)
print (forecast)

mm = round(10**((forecast['averagerain'] - 109)/32),2)
print (mm)
