from paho.mqtt import client as mqtt
import time
from os.path import exists
from os import system as com

# mqttBroker = '10.0.2.15'
while True:
    if(exists('server_start.lock') == True):
        client = mqtt.Client("c2")
        client.connect("127.0.0.1", port = 1883)                     
        client.loop_start()
        byteArray = bytes("a"*1000, 'utf-8')                                     
        client.publish(topic="chat", payload= byteArray,qos=2)
        # com('touch client_start.lock')
        time.sleep(3)
        client.loop_stop()
        break
    else:
        pass

com('rm server_start.lock')
com('touch client_end.lock')