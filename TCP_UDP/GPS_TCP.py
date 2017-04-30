from socket import *
from time import ctime

HOST="192.168.1.109"
PORT=21567
BUFSIZ=2048
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("Waiting for connection...")
    tcpCliSock,addr=tcpSerSock.accept()
    print("connectes from :",addr)

    while True:
        data=tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        i=bytes(data).decode('ascii')
        #i=str(data)
        print(i)
        print(data)
    tcpCliSock.close()
tcpCliSock.close()
