cmake_minimum_required(VERSION 2.8)
project( webcam )
add_compile_options(-std=c++11) # definitely needed!


find_package( OpenCV REQUIRED )
add_executable( webcam.out webcam.cpp) # SPECIFY .out HERE!!!
target_link_libraries( webcam.out ${OpenCV_LIBS} ) # SPECIFY .out HERE AS WELL!!!
