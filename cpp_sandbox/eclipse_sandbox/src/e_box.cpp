/*
 * e_box.cpp
 *
 *  Created on: May 28, 2018
 *      Author: kris
quick review of all things that have been done:
* set -std=c++11 flag
* set project to only release, not debug
* set include folders for ROS and opencv2

still missing:
* some sort of way to import properly config'd cmakelists
*
 */



#include <iostream>
#include <cstdlib>
#include "ros/ros.h"
#include <opencv2/core/core.hpp>
#include <time.h>

int main(){
	std::cout << "hello world" << std::endl;
	cv::Mat A;
//	A = cv::Mat(3,3,CV_32F);
//	A.at<float>(0,0) = 1;
	std::cout << "time is: "<< std::endl;
//	std::cout << "time is: "<< time() << std::endl;

	return 0;
}//int main
