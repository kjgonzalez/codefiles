#k260212: internet suggestions, need to improve and add best practices overall
# freeglut download: https://freeglut.sourceforge.net/
# specifically windows precompiled binaries, easy to use: https://www.transmissionzero.co.uk/software/freeglut-devel/
|# note, also saving it in this folder as backup

cmake_minimum_required(VERSION 3.15)
project(MyGLApp)

set(CMAKE_CXX_STANDARD 17)

# Tell CMake where FreeGLUT is
set(FREEGLUT_ROOT "C:/Packages/freeglut-3.0.0")

include_directories(${FREEGLUT_ROOT}/include)
link_directories(${FREEGLUT_ROOT}/lib/x64)

add_executable(MyGLApp main.cpp)

target_link_libraries(MyGLApp
    freeglut
    opengl32
    glu32
)
