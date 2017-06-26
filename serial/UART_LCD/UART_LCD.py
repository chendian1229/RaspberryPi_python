import binascii
import serial
import time

class LCD:
    def __init__(self,tag):
        self.tag=tag
        self.bus=serial.Serial('/dev/ttyUSB0',9600)
        
    def print_value(self,value):
        self.value=value
        self.print=self.tag+"=\""+str(self.value)+"\""
        self.print=self.print.encode("utf-8")
        self.bus.write(self.print)
        self.end_lcd()
        print(self.print)
        
    def end_lcd(self):
        self.bus.write(bytes.fromhex('ff'))
        self.bus.write(bytes.fromhex('ff'))
        self.bus.write(bytes.fromhex('ff'))
    def __del__(self):
        self.bus.close()
        print("Close the Serial")

if __name__=="__main__":
    try:
        tag1=LCD("t0.txt")
        tag1.print_value(234)
    except KeyboardInterrupt:
        del tag1
        print("Exit")
        
