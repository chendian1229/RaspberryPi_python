# -*- coding: utf-8 -*
import serial
import time
# 打开串口
ser = serial.Serial("/dev/ttyUSB0", 115200)

def showdata(arg):
    result = ''
    for i in arg:
        st = '%02X'%ord(i)
        result += st+' '
    print(result)


def main():
    while True:
        # 获得接收缓冲区字符
        count = ser.inWaiting()
        if count != 0:
            # 读取内容并回显
            recv = ser.read(count)
            print(type(recv),recv)
            r=str(recv)
            print(type(r),r)
            #showdata(recv)
            ser.write(recv)
        # 清空接收缓冲区
        ser.flushInput()
        # 必要的软件延时
        time.sleep(0.1)
   
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()
