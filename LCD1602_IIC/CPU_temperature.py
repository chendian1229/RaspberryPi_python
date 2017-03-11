#!/user/bin/env python 


import smbus
import time
import sys
import LCD1602 as LCD
temp=0


if __name__ == '__main__':
        LCD.init_lcd()
        LCD.print_lcd(0,0,'CPU T:%.2f'%temp)
        LCD.print_lcd(1,1,'wait a moment')
        print('wait 3 seconds')
        LCD.turn_light(1)
        time.sleep(3)
        try:
                while True:
                        file=open("/sys/class/thermal/thermal_zone0/temp")
                        temp=float(file.read())/1000
                        file.close()
                        LCD.print_lcd(0,0,'CPU T:%.2f'%temp)
                        nowtime = time.strftime('%m-%d %H:%M:%S',time.localtime(time.time()))
                        mintime = time.strftime('%M',time.localtime(time.time()))
                        print('current time:'+nowtime)
                        LCD.print_lcd(1,1,nowtime)
                        if mintime == 59:
                                LCD.turn_light(1)
                                print('mintime:'+mintime)	
                        time.sleep(1)
        except KeyboardInterrupt:
                LCD.print_lcd(0,1,'Can\'t see anyth')
        print('exit')
