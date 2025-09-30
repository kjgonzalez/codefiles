cmake_minimum_required(VERSION 3.30)
project(out)

# add eigen library =================
set(EIGEN3_INCLUDE_DIR "C:/Packages/eigen-3.4.0" CACHE PATH "Path to Eigen folder")
include_directories(${EIGEN3_INCLUDE_DIR})

file(GLOB SRCFILES "*.h" "*.cpp")

add_executable(out ${SRCFILES})
