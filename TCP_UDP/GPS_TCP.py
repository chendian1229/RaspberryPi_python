from socket import *
from time import ctime
import re

GPS_time=r'(\d{6}\.\d{3}\,)(\d{4}\.\d{5}\,N\,)(\d{5}\.\d{5}\,E)'
GPS_N=r'\d{4}\.\d{5}\,N'
GPS_E=r'\d{5}\.\d{5}\,E'

HOST="192.168.1.100"
PORT=21567
BUFSIZ=2048
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

def re_gps(re_demo,gps_source):
    gps_deal=re.search(re_demo,gps_source)
    return gps_deal

    
def display(time,east,north):
    if not (time or east or north):
        print('GPS signal-loss...')
    else:
        real_time=int(time.group(1)[0:6])+80000
        real_time=str(real_time)
        print(real_time[0:2]+':'+real_time[2:4],east.group(0),north.group(0))

        
def main():
    while True:
        print("Waiting for connection...")
        tcpCliSock,addr=tcpSerSock.accept()
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
        
