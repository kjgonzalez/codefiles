cmake_minimum_required(VERSION 3.20)
project(kmath)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# external libraries ===========
if(WIN32)
    message(STATUS "WINDOWS PLATFORM")
    set(EIGEN3_INCLUDE_DIR "C:/Pckgs/eigen-3.4.0" CACHE PATH "path")
elseif(UNIX)
    message(STATUS "LINUX PLATFORM")
    find_package(Eigen3 REQUIRED) # apt `libeigen3-dev`
else()
    message(FATAL_ERROR "UNSUPPORTED PLATFORM")
endif()

include_directories(${EIGEN3_INCLUDE_DIR}) # project-wide

# library ===============
add_library(
    mymath
    SHARED
    src/mymath.cpp
    )
target_compile_definitions(
    mymath
    PRIVATE
    )
target_include_directories(
    mymath
    PUBLIC
    include/
    )

# executable =============
add_executable(
    demo
    src/examples/demo.cpp # todo: moveme
    )
target_link_libraries(
    demo
    PRIVATE
    mymath
)

# post processing =========
# todo: copy lib & headers to another folder