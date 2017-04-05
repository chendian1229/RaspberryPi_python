#!/usr/bin/python  
#-*- coding: utf-8 -*-

import time  
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM) #使用BCM编码方式  
#定义引脚  
GPIO_TRIGGER = 21  
GPIO_ECHO    = 20  
#设置引脚为输入和输出  
GPIO.setwarnings(False)  
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger  
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo  
  
def dis():  #测距函数  
    GPIO.output(GPIO_TRIGGER, False) #设置trigger为低电平  
    time.sleep(0.5)  
    GPIO.output(GPIO_TRIGGER, True) #设置trigger为高电平  
    time.sleep(0.00001)  
    GPIO.output(GPIO_TRIGGER, False)  
    #start = time.time()  #记录发射超声波开始时间  
  
    while GPIO.input(GPIO_ECHO)==GPIO.LOW:  
        start = time.time()  
  
    while GPIO.input(GPIO_ECHO)==GPIO.HIGH:  
        stop = time.time()  #记录接收到超声波时间  
      
    elapsed = stop-start   #计算一共花费多长时间  
    distance = elapsed * 34300  #计算距离，就是时间乘以声速  
    distance = distance / 2  #除以2得到一次的距离而不是来回的距离  
    print ("Distance : %.1fcm" % distance  )
  
try:  #用于捕捉异常  
        while True:  
                dis()   #调用测距函数  
                time.sleep(0.5)  
except KeyboardInterrupt:  
        GPIO.cleanup() 
