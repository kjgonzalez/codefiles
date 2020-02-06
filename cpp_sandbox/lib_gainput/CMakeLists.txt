cmake_minimum_required(VERSION 3.0)
project(hello_gainput)

include_directories(~/programs/gainput/lib/)
include_directories(~/programs/gainput/lib/include/)
include_directories(~/programs/gainput/lib/include/gainput/)

file(GLOB_RECURSE sources *.cpp)

add_executable( hello_gainput.out keyinput.cpp) # SPECIFY .out HERE!!!
target_link_libraries(hello_gainput.out X11 GL rt)
target_link_libraries(hello_gainput.out gainputstatic)
