import _ctypes
from ctypes import (
    c_char_p,
    c_int32,
    c_size_t,
    c_void_p,
    cdll,
)
import os
import sys


class TfLiteInterface:
    def __init__(self, lib_path):
        assert os.path.exists(lib_path)
        self.lib = cdll.LoadLibrary(lib_path)

        self.TfLiteVersion = self.lib.TfLiteVersion
        self.TfLiteVersion.restype = c_char_p

        self.TfLiteModelCreateFromFile = self.lib.TfLiteModelCreateFromFile
        self.TfLiteModelCreateFromFile.argtypes = [c_char_p]
        self.TfLiteModelCreateFromFile.restype = c_void_p

        self.TfLiteInterpreterOptionsCreate = self.lib.TfLiteInterpreterOptionsCreate
        self.TfLiteInterpreterOptionsCreate.argtypes = []
        self.TfLiteInterpreterOptionsCreate.restype = c_void_p

        self.TfLiteInterpreterOptionsSetNumThreads = self.lib.TfLiteInterpreterOptionsSetNumThreads
        self.TfLiteInterpreterOptionsSetNumThreads.argtypes = [c_void_p, c_int32]

        self.TfLiteInterpreterCreate = self.lib.TfLiteInterpreterCreate
        self.TfLiteInterpreterCreate.argtypes = [c_void_p, c_void_p]
        self.TfLiteInterpreterCreate.restype = c_void_p

        self.TfLiteInterpreterAllocateTensors = self.lib.TfLiteInterpreterAllocateTensors
        self.TfLiteInterpreterAllocateTensors.argtypes = [c_void_p]

        self.TfLiteInterpreterGetInputTensor = self.lib.TfLiteInterpreterGetInputTensor
        self.TfLiteInterpreterGetInputTensor.argtypes = [c_void_p, c_int32]
        self.TfLiteInterpreterGetInputTensor.restype = c_void_p

        self.TfLiteTensorCopyFromBuffer = self.lib.TfLiteTensorCopyFromBuffer
        self.TfLiteTensorCopyFromBuffer.argtypes = [c_void_p, c_void_p, c_size_t]

        self.TfLiteInterpreterInvoke = self.lib.TfLiteInterpreterInvoke
        self.TfLiteInterpreterInvoke.argtypes = [c_void_p]

        self.TfLiteInterpreterGetOutputTensor = self.lib.TfLiteInterpreterGetOutputTensor
        self.TfLiteInterpreterGetOutputTensor.argtypes = [c_void_p, c_int32]
        self.TfLiteInterpreterGetOutputTensor.restype = c_void_p

        self.TfLiteTensorCopyToBuffer = self.lib.TfLiteTensorCopyToBuffer
        self.TfLiteTensorCopyToBuffer.argtypes = [c_void_p, c_void_p, c_size_t]

        self.TfLiteInterpreterDelete = self.lib.TfLiteInterpreterDelete
        self.TfLiteInterpreterDelete.argtypes = [c_void_p]

        self.TfLiteInterpreterOptionsDelete = self.lib.TfLiteInterpreterOptionsDelete
        self.TfLiteInterpreterOptionsDelete.argtypes = [c_void_p]

        self.TfLiteModelDelete = self.lib.TfLiteModelDelete
        self.TfLiteModelDelete.argtypes = [c_void_p]

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if sys.platform == "win32":
            _ctypes.FreeLibrary(self.lib._handle)
        else:
            _ctypes.dlclose(self.lib._handle)
