cmake_minimum_required(VERSION 2.8)
project(basicsample)

include_directories(~/programs/gainput/lib/)
include_directories(~/programs/gainput/lib/include/)
include_directories(~/programs/gainput/lib/include/gainput/)

file(GLOB_RECURSE sources *.cpp)

add_executable( sample.out basicsample_linux.cpp) # SPECIFY .out HERE!!!
target_link_libraries(sample.out X11 GL rt)
target_link_libraries(sample.out gainputstatic)
