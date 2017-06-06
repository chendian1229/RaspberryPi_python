from socket import*             #导入相应模块
from time import ctime
import re


GPS_time=r'(\d{6}\.\d{3}\,)(\d{4}\.\d{5}\,N\,)(\d{5}\.\d{5}\,E)'
GPS_N=r'\d{4}\.\d{5}\,N'        #提取相应GPS信息的正则表达式
GPS_E=r'\d{5}\.\d{5}\,E'

HOST="192.168.43.87"            #设置TCP服务器的IP地址，相应端口和缓存区大小
PORT=21567
BUFSIZ=2048
ADDR=(HOST,PORT)                #addr为IP和PORT端口

tcpSerSock=socket(AF_INET,SOCK_STREAM)      #TCP协议的套接字类型为SOCK_STREAM,AF_INET为socket_family
tcpSerSock.bind(ADDR)                       #设定TCP服务器地址
tcpSerSock.listen(5)                        #同时可链接5个客户端

'''
GPS的正则表达式提取函数
'''
def re_gps(re_demo,gps_source):
    gps_deal=re.search(re_demo,gps_source)
    return gps_deal

'''
GPS信息打印函数，输出经纬度信息和实时时间
'''
def display(time,east,north):
    if not (time or east or north):
        print('GPS signal-loss...')
    else:
        real_time=int(time.group(1)[0:6])+80000
        real_time=str(real_time)
        print(real_time[0:2]+':'+real_time[2:4],east.group(0),north.group(0))

'''
主函数，创建TCP服务器，建立连接
'''
def main():
    while True:
        print("Waiting for connection...")
        tcpCliSock,addr=tcpSerSock.accept()     #接收客户端传来信息     
        print("connectes from :",addr)          

        while True:
            data=tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            i=bytes(data).decode('ascii')
            North=re_gps(GPS_N,i)
            East=re_gps(GPS_E,i)
            Time=re_gps(GPS_time,i)
            display(Time,East,North)
            #print(i)
        tcpCliSock.close()
    tcpCliSock.close()
if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('The program runs to completion!')
        
