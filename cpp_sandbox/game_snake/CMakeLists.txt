cmake_minimum_required(VERSION 2.8)
project( game_snake )
add_compile_options(-std=c++11) # definitely needed!


find_package( OpenCV REQUIRED )
add_executable( snake.out snake.cpp) # SPECIFY .out HERE!!!
target_link_libraries( snake.out ${OpenCV_LIBS} ) # SPECIFY .out HERE AS WELL!!!
