import ctypes
m=ctypes.cdll.LoadLibrary
lib=m('./libpycall.so')
lib.foo(1,3)
print('OK')
