import serial
import time
import binascii

t=serial.Serial('/dev/ttyUSB0',9600)

def end_lcd(l):
    l.write(bytes.fromhex('ff'))
    l.write(bytes.fromhex('ff'))
    l.write(bytes.fromhex('ff'))

def main():
    for i in range(0,10):
        l=str(i)
        p="t0.txt=\""+l+"\""
        print(p)
        q=p.encode("utf-8")
        t.write(q)
        end_lcd(t)
        i=i+1
        time.sleep(1)
    
    
if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('exit')
        t.close()
    
    

