#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

SCRIPT_DIR=$(realpath ${0%/*})
cd $SCRIPT_DIR

TENSORFLOW_SRC_DIR=$(realpath $SCRIPT_DIR/tensorflow)

if [[ ! -d $TENSORFLOW_SRC_DIR ]]; then
  git clone --depth 1 --branch v2.9.0 https://github.com/tensorflow/tensorflow
  sed "s/common\\.c$/common\\.cc/" tensorflow/tensorflow/lite/c/CMakeLists.txt
fi

INCLUDE_DIR=$(realpath $SCRIPT_DIR/../include)
BUILD_DIR=$SCRIPT_DIR/build
OUTPUT_LIB_DIR=$(realpath $SCRIPT_DIR/../bin)

mkdir -p $BUILD_DIR
cd $BUILD_DIR
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1 -DCMAKE_C_FLAGS='-ffunction-sections -fdata-sections' -DCMAKE_CXX_FLAGS='-ffunction-sections -fdata-sections' $TENSORFLOW_SRC_DIR/tensorflow/lite/c
cmake --build . -j 7

mkdir -p $OUTPUT_LIB_DIR
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
