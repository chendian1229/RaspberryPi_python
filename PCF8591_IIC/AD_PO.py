#!/usr/bin/python
# -*- coding:utf-8 -*-

import smbus
import time

address=0x48
A0=0x40
A1=0x41
A2=0x42
A3=0x43
bus=smbus.SMBus(1)


if __name__=='__main__':
    try:
        while True:
            bus.write_byte(address,A3)
            value=bus.read_byte(address)
            print("AIN:%1.3f "%(value)*3.3/255))
            time.sleep(1)
    except KeyboardInterrupt:
        print('exit')



