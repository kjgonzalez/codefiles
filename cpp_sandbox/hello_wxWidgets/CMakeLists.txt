cmake_minimum_required(VERSION 3.0)
project( wx_attempt )
# add_compile_options(-std=c++11) # definitely needed!

# find_package(Eigen3 3.3 REQUIRED NO_MODULE)
# find_package( OpenCV REQUIRED )
find_package(wxWidgets REQUIRED COMPONENTS net core base)


include(${wxWidgets_USE_FILE})


add_executable( a.out wx_attempt.cpp) # SPECIFY .out HERE!!!

target_link_libraries(a.out
    ${wxWidgets_LIBRARIES})

# target_link_libraries(a.out
#     # Eigen3::Eigen
#     # ${OpenCV_LIBS}
#     ) # SPECIFY .out HERE AS WELL!!!
