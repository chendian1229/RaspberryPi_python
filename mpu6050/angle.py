from mpu6050 import mpu6050
import threading
import time
import math

angle_acc_init=0    #初始化由加速度得出的角度
angle_yjhb=0        #一阶互补滤波的初值
gyr_y_init=0        #y方向上的初值，用于消除陀螺仪温漂

sensor=mpu6050(0x68)        #设置从机地址为0x68


def cal_data(data):
    for i in range(100):
        accel_data=sensor.get_accel_data()      #获取加速度数据
        gyro_data=sensor.get_gyro_data()        #获取陀螺仪角速度数据

        data[0]=accel_data['x']+data[0]
        data[1]=accel_data['y']+data[1]
        data[2]=accel_data['z']+data[2]

        data[3]=gyro_data['x']+data[3]
        data[4]=gyro_data['y']+data[4]
        data[5]=gyro_data['z']+data[5]

    result=[x/100 for x in data]                #列表中每个元素整体除以100
    return result

def get_data(data):                         #获取数据函数，得到MPU6050数据
    accel_data=sensor.get_accel_data()      #获取加速度数据
    gyro_data=sensor.get_gyro_data()        #获取陀螺仪角速度数据
    data[0]=accel_data['x']
    data[1]=accel_data['y']
    data[2]=accel_data['z']

    data[3]=gyro_data['x']
    data[4]=gyro_data['y']
    data[5]=gyro_data['z']
    return data

def Init_MPU6050_data():                #初始化MPU6050，得出的初值
    global angle_yjhb
    global angle_acc_init
    global gyr_y_init
    data=[]
    mpu6050_init_data=[0,0,0,0,0,0]
    data=cal_data(mpu6050_init_data)        #计算100次平均后的值
    acc_x_init=data[0]*19.6133/32767        #转化为实际加速度的值M/s2
    acc_z_init=data[2]*19.6133/32767        #转化为实际加速度的值M/s2
    gyr_y_init=data[4]*250.0/32767          #转化为实际角速度 度/s

    angle_acc_init=math.atan2(acc_x_init,acc_z_init)*57.29578    #加速度解析出角度初值
    angle_yjhb=math.atan2(acc_x_init,acc_z_init)*57.29578        #一阶互补滤波前的初值

def fun_time():
    #定时器服务子函数
    global angle_yjhb
    global angle_acc_init
    global gyr_y_init

    K=0.12              #互补系数
    data=[]             #数据传回来的值
    mpu6050_data=[0,0,0,0,0,0]
    data=get_data(mpu6050_data)
    acc_x=data[0]*19.6133/32767         #转化为实际加速度的值M/s2
    acc_z=data[2]*19.6133/32767         #转化为实际加速度的值M/s2
    gyr_y=data[4]*250.0/32767           #转化为实际角速度 度/s
    
    gyr_y=round(gyr_y-gyr_y_init,6)             #消除陀螺仪温漂
    angel_acc=math.atan2(acc_x,acc_z)*57.29578  #加速度分解出当前角度
    angle_acc_init=angle_acc_init-gyr_y*0.01    #陀螺仪积分出来的当前角度
    angle_yjhb=K*angel_acc+(1-K)*(angle_yjhb-gyr_y*0.01)
    
    print('{0:^10.5f}\t{1:^10.5f}'.format(angel_acc,angle_yjhb))

    global timer                           #引入全局变量timer
    timer=threading.Timer(0.01,fun_time)   #设置递归调用定时器的函数
    timer.start()


def main():
    timer=threading.Timer(0.01,fun_time)       #设置定时器
    Init_MPU6050_data()                     #计算陀螺仪初值
    timer.start()                           #定时器开始计时


if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        timer.cancel()
    
