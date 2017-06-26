import ctypes
m=ctypes.cdll.LoadLibrary
lib=m('./test.so')
lib.argtype=(ctypes.c_float,ctypes.c_float)
lib.restype=ctypes.c_float
def main():
    k=lib.foo(l=1.1,o=2.2)
    print(k,"OK")

if __name__=="__main__":
    main()

    
