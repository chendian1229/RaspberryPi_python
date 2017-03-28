#!/user/bin/env python 

import socket
import smbus
import time
import sys
import LCD1602 as LCD

def Get_local_ip():
        try:
                csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                csock.connect(('8.8.8.8', 80))
                (addr, port) = csock.getsockname()
                csock.close()
                return addr
        except socket.error:
                return "127.0.0.1"



if __name__ == '__main__':  
        LCD.init_lcd()
        local_IP=Get_local_ip()
        LCD.print_lcd(0,0,'RaspberryPi IP')
        LCD.print_lcd(1,1,local_IP)
        LCD.turn_light(1)
        time.sleep(3)

