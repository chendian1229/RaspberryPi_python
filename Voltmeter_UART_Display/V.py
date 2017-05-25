#!/usr/bin/pyhon
# -*- coding:utf-8 -*-

import smbus
import time
import serial

t=serial.Serial('/dev/ttyUSB0',9600)
bus=smbus.SMBus(1)

address=0x48
#A0=0x40
#A1=0x41
#A2=0x42
A3=0x43

def end_lcd(l):
    l.write("\xff")
    l.write("\xff")
    l.write("\xff")
    
def main():
    bus.write_byte(address,A3)
    value=bus.read_byte(address)
    #print("AOUT:%1.3f "%(value*3.3/255))
    value=str(value*3.3/255)
    value="t0.txt=\""+value[0:5]+"\""
    t.write(value)
    end_lcd(t)
    time.sleep(0.1)

if __name__=='__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('exit')
        t.close()
