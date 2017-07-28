import ctypes
import time
m=ctypes.cdll.LoadLibrary
lib=m('./1.so')
lib.argtype=[ctypes.c_float,ctypes.c_float]
lib.restype=ctypes.c_float
def main():
    l1=2.3
    l2=3.2
    for i in range(10):
        k=lib.foo(l1,l2)
        print(k,"OK")
        time.sleep(0.5)

if __name__=="__main__":
    main()

    
