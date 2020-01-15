KJG200115: this folder to be used for HEAVY usage of ROS. small python-based scripts don't need to be put here, put them in py_sandbox. 

NOTE: when running things, be sure to source devel/setup.bash after "catkin_make" but before "rosrun"

general steps: 

# DEVELOP
cd ~/(???)/catkin_ws
catkin_create_pkg PkgName [dependencies...]
mkdir -p src/PkgName/src/ # or PkgName/scripts, depending on language
# (write some code)
# (if writing in cpp, modify CMakeLists.txt)
cd ~/(???)/catkin_ws
catkin_make


# RUN
roscore
source devel/setup.bash # make sure all packages are found # auto-generate
rosrun PkgName SpecificProgram(.py)





eof
