cmake_minimum_required(VERSION 3.0)
project( eigen_cmake )
add_compile_options(-std=c++11) # definitely needed!

find_package(Eigen3 3.3 REQUIRED NO_MODULE)
add_executable( eigen_cmake.out eigen_with_cmake.cpp) # SPECIFY .out HERE!!!
target_link_libraries( eigen_cmake.out Eigen3::Eigen) # SPECIFY .out HERE AS WELL!!!
