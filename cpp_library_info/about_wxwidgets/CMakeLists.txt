cmake_minimum_required(VERSION 3.20)
project(about_wxwidgets)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# external libraries ===========
if(WIN32)
    message(STATUS "WINDOWS PLATFORM")
    #set(EIGEN3_INCLUDE_DIR "C:/Pckgs/eigen-3.4.0" CACHE PATH "path") 
    # change above path in msvs: Project >> CMake Settings for <projname>


elseif(UNIX)
    message(STATUS "LINUX PLATFORM")
    find_package(Eigen3 REQUIRED) # apt `libeigen3-dev`
else()
    message(FATAL_ERROR "UNSUPPORTED PLATFORM")
endif()

# windows-specific way to compile wxwidgets
#set(CMAKE_MFC_FLAG 2)

#ADD_DEFINITIONS(-DUNICODE) # seems to help with getting unicode support
ADD_DEFINITIONS(-D_UNICODE)

set(wxWidgets_USE_STATIC ON)

find_package(wxWidgets REQUIRED COMPONENTS core base)

include(${wxWidgets_USE_FILE})



# executable =============
add_executable(demo1 WIN32 "src/examples/demo1.cpp") # todo: explain how to make functional on linux
target_link_libraries(demo1 PRIVATE ${wxWidgets_LIBRARIES})

#target_link_libraries(demo1 PRIVATE mymath)

# post processing =========
# todo: copy lib & headers to another folder