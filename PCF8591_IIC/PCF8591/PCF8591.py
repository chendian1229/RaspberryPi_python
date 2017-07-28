import smbus
import time

class AD:
    address=0x48    #默认地址
    A0=0x40         #AD转换通道，从A0到A3
    A1=0x41
    A2=0x42
    A3=0x43
    #默认PCF8591的地址为0x48,默认AD通道为0x40,即A0
    def __init__(self,address=0x48,channel=0x40):
        self.address=address
        self.channel=channel
        self.bus=smbus.SMBus(1)
    def get_value(self):
        self.bus.write_byte(self.address,self.channel)
        value=self.bus.read_byte(self.address)
        return value

class DA:
    address=0x48    #DA转换地址
    cmd=0x40        #DA转换命令字
    value=0         #初始化value
    #实例化一个DA的同时传入DA的value,简单易读
    def __init__(self,value):
        bus=smbus.SMBus(1)
        if value>255:       #异常处理，超出DA范围抛出异常
            raise Exception("DA数值超出范围")
        self.value=value
        bus.write_byte_data(self.address,self.cmd,self.value)
        

if __name__=="__main__":
    try:
        a=AD(channel=AD.A3)
        for i in range(10):
            s=a.get_value()
            print(s)
            time.sleep(0.5)
            
        for j in range(20,255):
            b=DA(j)
            time.sleep(0.02)
            
    except KeyboardInterrupt:
        del a
        del b
    
