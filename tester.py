import pcapy
from struct import *
import csv


devices = pcapy.findalldevs()
# ind = devices.index('wlan0')
loopback = devices[devices.index('lo')]

cap  = pcapy.open_live(loopback, 1024, 1, 5)


h, p = cap.next()
print(p)
