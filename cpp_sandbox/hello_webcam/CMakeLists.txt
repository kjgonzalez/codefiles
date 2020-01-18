cmake_minimum_required(VERSION 2.8)
project( webcam.out )
add_compile_options(-std=c++11) # definitely needed!


find_package( OpenCV REQUIRED )
add_executable( webcam webcam.cpp)
target_link_libraries( webcam.out ${OpenCV_LIBS} )
