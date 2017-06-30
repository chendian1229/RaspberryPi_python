import spidev
import time
from thermocouples_reference import thermocouples

typeK = thermocouples['K']

adc = spidev.SpiDev()
adc.open(0, 0)
adc.max_speed_hz = 1*10**6
adc.mode = 0x01

temp_config = [0b10111111, 0b00011011]
AIN1_config = [0b10001111, 0b00001011]
AIN2_config = [0b10111111, 0b00001011]

def signed_trans(high_byte, low_byte):
    num = high_byte*256+low_byte
    if num > (2**15-1):
        return (2**16-num)*(-1)
    else:
        return num

for i in range(1000):
    adc.xfer2(temp_config+temp_config)  # read Temp
    time.sleep(0.15)
    temp_result = adc.xfer2([0b00, 0b00])
    temp = (signed_trans(temp_result[0], temp_result[1])/4)*0.03125
    adc.xfer2(AIN1_config+AIN1_config) # AIN0+ AIN1-
    time.sleep(0.15)
    AIN1_result = adc.xfer2([0b00, 0b00])
    adc.xfer2(AIN2_config+AIN2_config) # AIN2+ AIN3- 
    time.sleep(0.15)
    AIN2_result = adc.xfer2([0b00, 0b00])
    AIN1_out = signed_trans(AIN1_result[0],AIN1_result[1])*7.8125 
    AIN2_out = signed_trans(AIN2_result[0],AIN2_result[1])*7.8125
    reading = typeK.inverse_CmV(AIN1_out/1000.0, Tref=temp)

    print("===============")
    #print(temp_result)
    #print(AIN1_result)
    #print(AIN2_result)
    print("ROOM Temp = {} C".format(temp))
    print("AIN1 = {} μV".format(AIN1_out))
    print("AIN2 = {} μV".format(AIN2_out))
    print("Reading Temp = {} C".format(reading))
adc.close()

