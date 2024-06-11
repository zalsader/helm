import ctypes

class HelmCmdReturnType(ctypes.Structure):
    _fields_ = [('r0', ctypes.c_longlong), ('r1', ctypes.c_char_p)]

helm = ctypes.cdll.LoadLibrary('./bin/helm.so')
helmCmd = helm.helmCmd
helmCmd.argtypes = [ctypes.c_char_p]
helmCmd.restype = HelmCmdReturnType
ret = helmCmd(b"helm list")
print(ret.r1.decode())
