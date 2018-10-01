//============================================================================
// Name        : e3.cpp
// Author      : KJG
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream> // I/O functions
#include <cstdlib>  // converter functions
#include <opencv2/core/core.hpp>	// cv libraries
//using namespace std;

int main(int argc, char *argv[]) {
	std::cout << "!!!Hello World!!!" << std::endl;
	cv::Mat A(3,3,CV_64F);
	A.at<double>(0,0) = 2;




	return 0;
}
