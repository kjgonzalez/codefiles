cmake_minimum_required(VERSION 2.8)
project( eigen_cmake )
add_compile_options(-std=c++11 -I ~/programs/eigen/) # definitely needed!


# find_package( OpenCV REQUIRED )
add_executable( eigen_cmake.out eigen_with_cmake.cpp) # SPECIFY .out HERE!!!
target_link_libraries( eigen_cmake.out ) # SPECIFY .out HERE AS WELL!!!
# ${OpenCV_LIBS}
