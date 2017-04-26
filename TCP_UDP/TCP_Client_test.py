from socket import *

HOST="192.168.43.43"            #创建localhost
PORT=8083
BUFSIZ=1024
ADDR=(HOST,PORT)


tcpCliSock=socket(AF_INET,SOCK_STREAM) #创建套接字
tcpCliSock.connect(ADDR)

while True:
    data=input(">")
    data=data.encode(encoding="utf-8")  #sock.send()中必须为bytes，则字符串转化为bytes
    tcpCliSock.send(data)
    h=tcpCliSock.recv(BUFSIZ)
    if not h:
        break
    print(h)

tcpCliSock.close()
