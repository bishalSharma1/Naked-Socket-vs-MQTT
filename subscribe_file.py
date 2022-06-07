import paho.mqtt.client as mqtt
from os.path import exists
import time
import os

ind = False

def on_message(client, obj, msg):                             
  with open('file_to_receive.txt', 'wb') as f:
    f.write(msg.payload)
  print("file banyo")
  global ind
  ind = True

def on_dis(cl, ud, rc = 0):
  client.loop_stop()
  print("disconnected")

client = mqtt.Client("c2")                                
client.connect("127.0.0.1", port = 1883)             
client.subscribe("file", qos=2)
print("Starting Server...")
client.loop_start()

os.system("touch server_start.lock")

print('Waiting message...')
while True:
  client.on_message = on_message
  if(ind == True):
    os.system('touch banyo.lock')
    break

while True:
  if exists('client_end.lock') == True:
    break

client.on_disconnect = on_dis
client.loop_stop()

os.system('rm banyo.lock')
os.system('rm server_start.lock')
os.system('rm file_to_receive.txt')
os.system('touch server_end.lock')