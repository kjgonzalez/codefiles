# basic ini parser

cmake_minimum_required(VERSION 3.25)
set(CMAKE_CXX_STANDARD 17)
project(kiniparse)

#target_compile_definitions(test_kiniparse BASEPATH="${CMAKE_SOURCE_DIR}")
add_compile_definitions(BASEPATH="${CMAKE_SOURCE_DIR}")

add_executable(test_kiniparse test_kiniparse.cpp)
