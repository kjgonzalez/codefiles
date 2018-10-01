################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../src/e_box.cpp 

OBJS += \
./src/e_box.o 

CPP_DEPS += \
./src/e_box.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C++ Compiler'
	g++ -I/opt/ros/kinetic/include -I/usr/local/include/opencv2 -include"/usr/local/lib -lopencv_ml -lopencv_stitching -lopencv_dnn -lopencv_superres -lopencv_shape -lopencv_viz -lopencv_videostab -lopencv_video -lopencv_photo -lopencv_calib3d -lopencv_features2d -lopencv_highgui -lopencv_videoio -lopencv_imgcodecs -lopencv_flann -lopencv_objdetect -lopencv_imgproc -lopencv_core" -O3 -Wall -c -fmessage-length=0 -std=c++11 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


