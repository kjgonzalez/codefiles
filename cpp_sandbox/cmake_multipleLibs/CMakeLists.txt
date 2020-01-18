cmake_minimum_required(VERSION 3.0)
project( cmake_multilib )
add_compile_options(-std=c++11) # definitely needed!

find_package(Eigen3 3.3 REQUIRED NO_MODULE)
find_package( OpenCV REQUIRED )

add_executable( cmake_multilib.out cmake_multiLib.cpp) # SPECIFY .out HERE!!!
target_link_libraries(cmake_multilib.out 
    Eigen3::Eigen 
    ${OpenCV_LIBS}
    ) # SPECIFY .out HERE AS WELL!!!
