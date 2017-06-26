#!/usr/bin/env python
"""Released under the MIT License
Copyright 2015, 2016 MrTijn/Tijndagamer
"""

from mpu6050 import mpu6050
from time import sleep

sensor = mpu6050(0x68)

while True:
    accel_data = sensor.get_accel_data()
    gyro_data = sensor.get_gyro_data()
    temp = sensor.get_temp()

    print("Accelerometer data")
    print("x: " , accel_data['x'],type(accel_data['x']))
    print("y: " , accel_data['y'])
    print("z: " , accel_data['z'])

    print("Gyroscope data")
    print("x: " , gyro_data['x'])
    print("y: " , gyro_data['y'])
    print("z: " , gyro_data['z'])

    #print("Temp: " + str(temp) + " C")
    sleep(2)
