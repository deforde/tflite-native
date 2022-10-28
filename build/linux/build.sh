#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

OUTPUT_LIB_VERSION=0.1.0

HOME=/home/mruser
TENSORFLOW_SRC_DIR=$HOME/tensorflow
INCLUDE_DIR=$HOME/include
BUILD_DIR=$HOME/build
OUTPUT_LIB_DIR=$HOME/bin

rm -rf $BUILD_DIR
mkdir -p $BUILD_DIR
cd $BUILD_DIR

PLATFORM="linux"
# We assume that the host system is an x86_64 machine
ARCH="x86_64"
CMAKE_ARGS="-DCMAKE_EXPORT_COMPILE_COMMANDS=1 -DCMAKE_C_FLAGS='-ffunction-sections -fdata-sections' -DCMAKE_CXX_FLAGS='-ffunction-sections -fdata-sections'"
eval "cmake $CMAKE_ARGS ../tensorflow/tensorflow/lite/c"
cmake --build . -j 7

mv libtensorflowlite_c.so $OUTPUT_LIB_DIR
