# basic usage, including on windows: 
# 1. mdkir build
# 2. cd build
# 3. cmake ..
# 4a. if on linux: make
# 4b. if on windows: msbuild out.sln
# 5. (run program)

cmake_minimum_required(VERSION 3.30) # 3.30.5 is installed on xps for msvc
project(out)

file(GLOB SRCFILES "*.h" "*.cpp")

add_executable(out ${SRCFILES})



