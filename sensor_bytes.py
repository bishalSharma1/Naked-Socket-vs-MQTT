from paho.mqtt import client as mqtt
import time
from os.path import exists
from os import system as com

# mqttBroker = '10.0.2.15'
while True:
    if(exists('server_start.lock') == True):
        client = mqtt.Client("Temperature")
        client.connect("127.0.0.1", port = 1883)                     
        client.loop_start()
                                                
        byteArray = bytes("a", 'utf-8')                                     
        client.publish(topic="chat", payload= byteArray,qos=2)
        time.sleep(1)
        client.loop_stop()

        com('rm server_start.lock')
        com('touch client_close.lock')
        break
    else:
        pass