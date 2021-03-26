import serial
import time
import os

a = 1
b = 2
c = 3
d = 4
e = 5

def send2Pd(message=''):
    os.system("echo '" + message + "' | pdsend 3000 localhost udp")

while True:
    
    send2Pd(str(a))

    time.sleep(0.5)
