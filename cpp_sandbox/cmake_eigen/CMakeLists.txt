cmake_minimum_required(VERSION 3.0)
project( cmake_eigen )
add_compile_options(-std=c++11) # definitely needed!

find_package(Eigen3 3.3 REQUIRED NO_MODULE)
add_executable( cmake_eigen.out cmake_eigen.cpp) # SPECIFY .out HERE!!!
target_link_libraries( cmake_eigen.out Eigen3::Eigen) # SPECIFY .out HERE AS WELL!!!
