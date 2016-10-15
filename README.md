A python3 wrapper for getting precipitation forecasts from http://www.buienradar.nl.
Returns a python dictionary with raw forecast data or total and average within a configurable timeframe.

Example usage:

```
import pybuienradar
import time

now = time.strftime("%H:%M")
timeframe = 3600
latitude = '52.0893191'
longitude = '5.110169100000007'

buienradar = pybuienradar.forecast(latitude, longitude)
forecast_data = buienradar.get_forecast_data()
forecast = buienradar.get_forecast(now, timeframe)

print (forecast_data)
print (forecast)
```
