from paho.mqtt import client as mqtt
import time
from os.path import exists

# mqttBroker = '10.0.2.15'
client = mqtt.Client("Temperature")                                
client.connect("127.0.0.1", port = 1883)                     
client.loop_start()

file = open("/home/bishal/Desktop/MQTT/sharma_tori/test.uxp", "rb")         
data = file.read()                                            
byteArray = bytes(data)                                       
client.publish(topic="uxp file", payload= byteArray,qos=2)
while True:
    if (exists('test1883.uxp') == True):
        break
