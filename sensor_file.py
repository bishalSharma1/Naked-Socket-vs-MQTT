from paho.mqtt import client as mqtt
import time
import os
from os.path import exists

with open('file_to_send.txt', "rb") as f:
    data = f.read()

while True:
    if exists("server_start.lock") == True:
        client = mqtt.Client("c1")
        client.connect("127.0.0.1", port = 1883)
        client.loop_start()
        client.publish(topic="file", payload= data, qos=2)
        while True:
            if exists('banyo.lock') == True:
                os.system('touch client_end.lock')
                break
        client.loop_stop()
        break
    else:
        pass
