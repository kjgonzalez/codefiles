/*
author: Kris Gonzalez
date: 200118
objective: using cmake, compile code that uses eigen, opencv and gainput

stat | descrip
done | hello world
done | compile with eigen
done | compile with opencv
done | compile with gainput
 
*/

#include <iostream>
#include <Eigen/Dense>                  // eigen library
#include <opencv2/core/core.hpp>        // cpp libraries
#include <opencv2/imgcodecs.hpp>        // ...
#include <opencv2/highgui/highgui.hpp>  // ...
#include <opencv2/core/mat.hpp>         // ...
#include <gainput/gainput.h>    // gainput library

using Eigen::MatrixXd;

int main(){
    std::printf("Eigen Matrix\n");
    MatrixXd m(2,2);
    m(0,0) = 3;
    m(1,0) = 2.5;
    m(0,1) = -1;
    m(1,1) = m(1,0) + m(0,1);
    std::cout << m << std::endl;
    
    std::printf("OpenCV Matrix\n");
    float a[3][3] = {{1,2,1},{7,9,6},{1,5,7}};
    cv::Mat A(3,3,CV_32F);
    A = cv::Mat(3,3,CV_32F,a);
    std::cout << A.t() << '\n'; // transpose operation here
    
    std::printf("Initialize gainput lib\n");
    
}
