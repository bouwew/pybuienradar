# coding: utf-8
import pybuienradar
import paho.mqtt.client as paho
import time
import json

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
    print(json.dumps(prediction))

# pybuienradar
offset = 3600
latitude = 52.151682
longitude = 6.064496
buienradar = pybuienradar.rainprediction(latitude, longitude)
prediction = buienradar.calculatetotalandaverage(offset)

# MQTT
client = paho.Client()
client.on_publish = on_publish
client.username_pw_set("username", "password")
client.connect("mqttbroker", 1883)
client.loop_start()

while True:
    (rc, mid) = client.publish("buienradar/prediction", json.dumps((prediction), sort_keys=True), qos=1)
    time.sleep(600)
