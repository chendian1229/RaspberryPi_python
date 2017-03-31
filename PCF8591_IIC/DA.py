#!/usr/bin/python
# -*- coding:utf-8 -*-

import smbus
import time

address=0x48
cmd=0x40
value=0

bus=smbus.SMBus(1)
if __name__=="__main__":
    try:
        while True:
            bus.write_byte_data(address,cmd,value)
            value+=1
            if value==256:
                value=1
            #print("AOUT:%3d"%value)
            time.sleep(0.01)
    except:
        print('exit')

    
