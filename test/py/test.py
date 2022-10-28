#!/usr/bin/env python3

from ctypes import (
    c_float,
    c_uint8,
    sizeof,
)
import os

from lq.tflite import TfLiteInterface


_LIB_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "bin", "libtensorflowlite_c.so")
_MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "model", "model.tflite")

with TfLiteInterface(_LIB_PATH) as tflite:
    var = tflite.TfLiteVersion().decode("utf-8")
    print(var)

    model = tflite.TfLiteModelCreateFromFile(bytes(_MODEL_PATH, encoding="utf-8"))
    assert model != 0

    options = tflite.TfLiteInterpreterOptionsCreate()

    tflite.TfLiteInterpreterOptionsSetNumThreads(options, 2)

    interpreter = tflite.TfLiteInterpreterCreate(model, options)

    status = tflite.TfLiteInterpreterAllocateTensors(interpreter)
    assert status == 0

    input_tensor = tflite.TfLiteInterpreterGetInputTensor(interpreter, 0)

    input_data = b"\0"

    status = tflite.TfLiteTensorCopyFromBuffer(input_tensor, input_data, 1)
    assert status == 0

    status = tflite.TfLiteInterpreterInvoke(interpreter)

    output_tensor = tflite.TfLiteInterpreterGetOutputTensor(interpreter, 0)
    output_arr = (c_uint8 * 1)()
    status = tflite.TfLiteTensorCopyToBuffer(
        output_tensor, output_arr, 1 * sizeof(c_uint8)
    )

    tflite.TfLiteInterpreterDelete(interpreter)
    tflite.TfLiteInterpreterOptionsDelete(options)
    tflite.TfLiteModelDelete(model)

    print("tested OK")
