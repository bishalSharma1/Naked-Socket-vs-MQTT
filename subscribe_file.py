from numpy import true_divide
import paho.mqtt.client as mqtt
import time
from os import system as com
from os.path import exists

ind = False

def on_message(client, obj, msg):
  with open("file_to_receive.txt", "wb") as f:
    f.write(msg.payload)
  global ind 
  ind = True

def on_dis(cl, ud, rc = 0):
  client.loop_stop()
  print("disconnected")


client = mqtt.Client("c1")
client.connect("127.0.0.1", port = 1883)             
client.subscribe("chat", qos=0)
print("Starting")
client.loop_start()
print('waiting message')
com('touch server_start.lock')
while True:
  client.on_message = on_message
  if ind == True:
    break
client.on_disconnect = on_dis
client.loop_stop()

com('touch server_end.lock')