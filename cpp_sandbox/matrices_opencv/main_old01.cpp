/*
 Author: Kris Gonzalez
 Date Created: 180519
 Objectives: practice / review general c++ concepts, then later move to ros
    / catkin side.

 topics:
 functions - done
 objects - done
 commandline args - done
 matrices

*/

// initializations /////////////////////////////////////////////////////////////
#include <iostream>  // typical io functions
#include <random>    // rand library
#include <cstdlib>   // contains converter functions
#include <opencv2/core/core.hpp>        // cpp libraries
#include <opencv2/imgcodecs.hpp>        // ...
#include <opencv2/highgui/highgui.hpp>  // ...
#include <opencv2/core/mat.hpp>

#define endl "\n"
// functions  //////////////////////////////////////////////////////////////////
float pyt(float a,float b){ // typical function definition
    return pow(a*a+b*b,0.5);
}//pyt

float delayedfn(); // this function is declared up top, then defined below


//will make small class for a rectangle that has properties and methods
class rect{
    //these are private by default
    int x, y;
    void setZero(){
            //sets both variables to 0
            //kjgnote: this is a private function
            x = 0;
            y = 0;
    } //make3
public:
    void set_values(int a,int b){
        x = a;
        y = b;
    }//set values

    int area(){
        return x*y;
    }//area
}; //class rect



// main code ///////////////////////////////////////////////////////////////////


int main(int argc, char *argv[]) {
    //kjgnote: argv works very similar to argv in python. argv[1] is the first argument
    std::cout << "Hello, World!" << endl;
    std::cout << "answer is " << pyt(3,4) << endl;

    rect box;
    box.set_values(3,4);

    if(argc==3){
        // assume that user only gives 2 arguments if they want to run pyt
        float aa = atof(argv[1]);
        float bb = atof(argv[2]);

        std::cout << "answer is" << pyt(aa,bb)<<endl;
    } // if statement

    // want to perform matrix operations, so will try out opencv \
        library, which should be good enough for now. let's see.

    cv::Mat A(3,3,CV_32F);
    A.at<double>(0,0) = 1;
//    A.at[0,0] = 1;
//    A[1][1] = 1;
//    A[2][2] = 1;



//    std::string imgname("./beach.jpg"); // default name
//    if(argc ==2) imgname = argv[1];
//    std::string st = "this is a string\n";
//    std::cout << st;
//    cv::Mat image; //declare image
//    image = cv::imread(imgname.c_str(), cv::IMREAD_COLOR); //read file
//
//    cv::namedWindow("fig1",cv::WINDOW_AUTOSIZE); //display
//    cv::imshow("fig1",image);
//    cv::waitKey(0);











    return 0; //end code

}//main

float delayedfn(){
    return 3;
}//delayedfn











//eof
