import ctypes
import os

_file="1.so"
_path=os.path.join(*(os.path.split(__file__)[:-1]+(_file,)))
_mod=ctypes.cdll.LoadLibrary(_path)

class parameter(ctypes.Structure):
    _fields_=[('P',ctypes.c_double),
              ('I',ctypes.c_double),
              ('D',ctypes.c_double)]

PID=_mod.PID
PID.argtype=parameter
PID.restype=ctypes.c_double
