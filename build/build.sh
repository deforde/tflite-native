#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

HOME=/home/mruser
TENSORFLOW_SRC_DIR=$HOME/tensorflow
INCLUDE_DIR=$HOME/include
BUILD_DIR=$HOME/build
OUTPUT_LIB_DIR=$HOME/bin

rm -rf $BUILD_DIR
mkdir -p $BUILD_DIR
cd $BUILD_DIR

CMAKE_ARGS="-DCMAKE_EXPORT_COMPILE_COMMANDS=1 -DCMAKE_C_FLAGS='-ffunction-sections -fdata-sections' -DCMAKE_CXX_FLAGS='-ffunction-sections -fdata-sections'"
eval "cmake $CMAKE_ARGS $TENSORFLOW_SRC_DIR/tensorflow/lite/c"
cmake --build . -j 7

mv libtensorflowlite_c.so $OUTPUT_LIB_DIR

cd $INCLUDE_DIR
cd $TENSORFLOW_SRC_DIR
HEADERS=$(find . -name "*.h")
for HEADER in $HEADERS; do
  HEADER_DIR=$(dirname $HEADER)
  mkdir -p $INCLUDE_DIR/$HEADER_DIR
  cp $HEADER $INCLUDE_DIR/$HEADER_DIR
done
cd $BUILD_DIR
HEADERS=$(find . -name "*.h")
for HEADER in $HEADERS; do
  HEADER_DIR=$(dirname $HEADER)
  mkdir -p $INCLUDE_DIR/$HEADER_DIR
  cp $HEADER $INCLUDE_DIR/$HEADER_DIR
done
