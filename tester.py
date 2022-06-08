# import pcapy
# from struct import *
# import csv
# import socket

# ip = socket.gethostbyname(socket.gethostname())


# # devices = pcapy.findalldevs()
# # # ind = devices.index('wlan0')
# # loopback = devices[devices.index('lo')]

# # cap  = pcapy.open_live(loopback, 1024, 1, 5)


# # h, p = cap.next()
# print(ip)


with open("file_to_send.txt", "wb") as f:
    byte_seq = bytes('a', 'utf-8')
    f.write(byte_seq * 1)