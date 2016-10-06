A python3 wrapper for getting the rainprediction from http://www.buienradar.nl in a python dictionary

Example usage:

```
import pybuienradar

offset = 3600

buienradar = pybuienradar.rainprediction(52.0893191, 5.110169100000007)
willitrain = buienradar.getprediction()
howmuch = buienradar.calculatetotalandaverage(offset)

print (willitrain)
print (howmuch)
```

