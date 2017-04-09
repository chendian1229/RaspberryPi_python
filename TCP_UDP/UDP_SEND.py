import socket   
import time
 
DST_IP = "192.168.1.110"
DST_PORT = 8080
 
#建立Socket，SOCK_DGRAM表示Socket类型为UDP
print("Starting socket: UDP...")
socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
#向目的地址和端口，发送数据
print("Sending package to %s:%d..." %(DST_IP, DST_PORT))
dst_addr = (DST_IP, DST_PORT)
while True:
        socket_udp.sendto("Hello UDP!",dst_addr)
        time.sleep(1) 
        continue
