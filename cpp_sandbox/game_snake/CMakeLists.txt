cmake_minimum_required(VERSION 3.0)
project( game_snake )
add_compile_options(-std=c++11) # definitely needed!

find_package( Eigen3 3.3 REQUIRED NO_MODULE )
find_package( OpenCV REQUIRED )
# no need to specify gainput???

add_executable( snake.out snake.cpp) # SPECIFY .out HERE!!!
target_link_libraries( snake.out 
    ${OpenCV_LIBS} 
    Eigen3::Eigen
    # for some reason, no need to specify gainput???
) # SPECIFY .out HERE AS WELL!!!
