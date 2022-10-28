#include <assert.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "tensorflow/lite/c/c_api.h"

#define TFLITE_CHECK(func_call) assert((func_call) == kTfLiteOk);

int main() {
  TfLiteModel *model = TfLiteModelCreateFromFile("../../model/model.tflite");
  TfLiteInterpreterOptions* options = TfLiteInterpreterOptionsCreate();
  TfLiteInterpreterOptionsSetNumThreads(options, 2);

  TfLiteInterpreter* interpreter = TfLiteInterpreterCreate(model, options);

  TFLITE_CHECK(TfLiteInterpreterAllocateTensors(interpreter));
  TfLiteTensor* input_tensor = TfLiteInterpreterGetInputTensor(interpreter, 0);

  uint8_t input[1] = {0};

  TFLITE_CHECK(TfLiteTensorCopyFromBuffer(input_tensor, input, sizeof(input)));

  TFLITE_CHECK(TfLiteInterpreterInvoke(interpreter));

  const TfLiteTensor* output_tensor = TfLiteInterpreterGetOutputTensor(interpreter, 0);
  uint8_t output[1] = {0};
  TFLITE_CHECK(TfLiteTensorCopyToBuffer(output_tensor, output, sizeof(output)));

  puts("tested OK!");

  return 0;
}
