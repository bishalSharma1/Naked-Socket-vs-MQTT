import paho.mqtt.client as mqtt
from os.path import exists
import time


def on_message(client, obj, msg):                             
  with open('/home/bishal/Desktop/MQTT/sharma_tori/test1883.uxp', 'wb') as f:
    f.write(msg.payload)
  print("file banyo")

def on_dis(cl, ud, rc = 0):
  client.loop_stop()
  print("disconnected")

client = mqtt.Client("Receiving Client1")                                
client.connect("127.0.0.1", port = 1883)             
client.subscribe("uxp file", qos=2)
print("Starting")
client.loop_start()
print('waiting message')
while True:
  client.on_message = on_message
  ex = exists('test1883.uxp')
  if ex == True:
    break
client.on_disconnect = on_dis
client.loop_stop()
