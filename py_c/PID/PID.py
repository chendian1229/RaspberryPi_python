import ctypes
import os

_file="libpycall.so"
_path=os.path.join(*(os.path.split(__file__)[:-1]+(_file,)))
_mod=ctypes.cdll.LoadLibrary(_path)

class parameter(ctypes.Structure):
    _fields_=[('P',ctypes.c_float),
              ('I',ctypes.c_float),
              ('D',ctypes.c_float)]

PID=_mod.PID
PID.argtype=parameter
PID.restype=ctypes.c_float
