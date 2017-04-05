import RPi.GPIO as GPIO
import time


i=[0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.IN)
GPIO.setup(21,GPIO.IN)
GPIO.setup(16,GPIO.IN)

def gpio20_isr(channel):
    if (GPIO.input(21)==GPIO.HIGH):
        i[0]=i[0]+1
    else:
        i[0]=i[0]-1    

def gpio21_isr(channel):
    if(GPIO.input(20)==GPIO.LOW):
        i[0]=i[0]+1
    else:
        i[0]=i[0]-1

def gpio16_isr(channel):
    i[0]=0
    
GPIO.add_event_detect(20,GPIO.RISING,callback=gpio20_isr,bouncetime=200)
GPIO.add_event_detect(21,GPIO.RISING,callback=gpio21_isr,bouncetime=200)
GPIO.add_event_detect(16,GPIO.FALLING,callback=gpio16_isr,bouncetime=200)

if __name__=='__main__':
    try:
        while True:
            print(i[0])
            time.sleep(0.5)
    except KeyboardInterrupt:
        print('exit')
        GPIO.cleanup()
    
