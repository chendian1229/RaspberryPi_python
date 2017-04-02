#!/usr/bin/pyhon
# -*- coding:utf-8 -*-

#导入模块
import smbus	#IIC
import time	
import serial	#串口屏幕
import LCD1602 as LCD　

t=serial.Serial('/dev/ttyUSB0',9600)
bus=smbus.SMBus(1)

address=0x48
#A0=0x40
#A1=0x41
#A2=0x42
A3=0x43

def end_uart_lcd(l):
    l.write("\xff")
    l.write("\xff")
    l.write("\xff")
    
def LCD_Init():
    LCD.init_lcd()
    LCD.print_lcd(0,0,'RaspberryPi IIC')
    #LCD.print_lcd(1,1,'wait a moment')
    LCD.turn_light(1)
    time.sleep(1.5)
    
def main():
    bus.write_byte(address,A3)
    value=bus.read_byte(address)
    #print("AOUT:%1.3f "%(value*3.3/255))
    value=str(value*3.3/255)
    
    LCD.print_lcd(1,1,value[0:5])
    LCD.print_lcd(7,1,"V")
    
    display="t0.txt=\""+value[0:5]+"V\""
    t.write(display)
    end_uart_lcd(t)
    time.sleep(0.1)

if __name__=='__main__':
    try:
        LCD_Init()
        while True:
            main()
    except KeyboardInterrupt:
        print('exit')
        t.close()
