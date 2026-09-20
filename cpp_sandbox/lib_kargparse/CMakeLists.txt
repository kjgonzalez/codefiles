# basic argument parser 

cmake_minimum_required(VERSION 3.20)
project(kargparse)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(test_kargparse "test_kargparse.cpp" "kargparse.hpp")

add_executable(demo "demo.cpp" "kargparse.hpp")


# eof
