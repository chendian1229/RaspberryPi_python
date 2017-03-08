#-*-coding: utf-8 -*-
#!/usr/bin/python
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
#GPIO.output(12,GPIO.HIGH)
p=GPIO.PWM(12,50)
p.start(0)
temp_last=0
try:
    while 1:
        time.sleep(1)
        file=open("/sys/class/thermal/thermal_zone0/temp")
        temp=float(file.read())/1000
        file.close()

        if temp>53:
            if temp_last>53:
                p.ChangeDutyCycle(40)
            time.sleep(0.1)
        elif temp>65:
            p.ChangeDutyCycle(20)
        else:
            if temp_last<=49.5:
                p.ChangeDutyCycle(100)
            time.sleep(0.1)
        #print(temp)
        temp_last=temp
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
print ("exit")




