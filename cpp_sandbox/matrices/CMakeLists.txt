cmake_minimum_required(VERSION 2.8) # note: 2.8 and above acceptable?
project(output)
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS} )

set(CMAKE_CXX_STANDARD 11)

add_executable(output main.cpp)
target_link_libraries( output ${OpenCV_LIBS} )
