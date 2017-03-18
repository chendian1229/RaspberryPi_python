import serial  
  
def hexShow(argv):  
    result = ''  
    hLen = len(argv)  
    for i in xrange(hLen):  
        hvol = ord(argv[i])  
        hhex = '%02x'%hvol  
        result += hhex+' '  
    print 'hexShow:',result
  
t = serial.Serial("/dev/ttyUSB0", 115200)  
#print t.portstr  
strInput = raw_input('enter some words:')  
n = t.write(strInput)  
print n 
str = t.read(n)  
print str  
hexShow(str) 
