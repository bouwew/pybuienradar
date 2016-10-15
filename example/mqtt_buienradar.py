# coding: utf-8
import pybuienradar
import paho.mqtt.client as paho
import time
import json

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
    print(json.dumps(forecast))

# pybuienradar
timeframe = 3600
latitude = 52.151682
longitude = 6.064496
buienradar = pybuienradar.forecast(latitude, longitude)

# MQTT
client = paho.Client()
client.on_publish = on_publish
client.username_pw_set("username", "password")
client.connect("mqttbroker", 1883)
client.loop_start()

while True:
    now = time.strftime("%H:%M")
    forecast = buienradar.get_forecast(now, timeframe)
    (rc, mid) = client.publish("buienradar/forecast", json.dumps((forecast), sort_keys=True), qos=1)
    time.sleep(600)
