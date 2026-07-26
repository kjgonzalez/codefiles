# basic ini parser when starting a project with a basic config file

cmake_minimum_required(VERSION 3.20)
project(kiniparse)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_compile_definitions(BASEPATH="${CMAKE_SOURCE_DIR}")

add_executable(
    test_kiniparse
    "test_kiniparse.cpp"
    "kiniparse.hpp"
)
