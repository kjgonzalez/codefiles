/*
 Author: Kris Gonzalez
 Date Created: 180519
 Objectives: practice / review general c++ concepts, then later move to ros
    / catkin side.

 topics:
 functions - done
 objects - done
 commandline args - done
 matrices - semi-done

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

	  //how does one assign a vector of values.?

    // quick practice on c++ vectors:
    // for more info: http://www.cplusplus.com/reference/vector/vector/
    std::vector<double> vec(3);
    std::cout << "vector length is "<< vec.size() << endl;
    //list all elements of vector:
    for(int i=0;i<vec.size();i++){
      std::cout << vec[i] <<endl;
    }//for-list all vector elements

    // a little bit of matrix stuff now.
    cv::Mat A(3,3,CV_32F);
    /*
    KJGNOTE: 32F is float, 64F is double. python has clearly made you lazy, you
    were getting type errors because you would create a float matrix and access
    with a double argument.
    */
    A.at<float>(0,0) = 1.0; //single element assignment
    std::cout << "this is a test" << endl;
    A.at<float>(1,1) = 1.0; //single element assignment
    A.at<float>(2,2) = 1.0; //single element assignment
    float a[3][3] = {{1,2,1},{7,9,6},{1,5,7}};
    A = cv::Mat(3,3,CV_32F,a);
    std::cout << A.t() << '\n';

    //kjgnote: another way to make everything go together:
    // cv::Mat I = cv::Mat::eye(3,3,CV_32F);
    // std::cout << "I"<<I << '\n';


    cv::Mat x(3,1,CV_32F);
    x.at<float>(0,0) = 2;
    x.at<float>(1,0) = 1;
    x.at<float>(2,0) = 3;
    std::cout << x << '\n';
    // A.at<double>(1,1) = 2;
    // A.at<double>(2,2) = 3;

    std::cout << "result of multiplying both is:" << '\n';
    std::cout << A*x << '\n';
    // try printing out the matrix somehow
    // std::cout << A << endl;
    // std::cout << A.size() << endl;
    // double m[3][3] = {{a, b, c}, {d, e, f}, {g, h, i}};
    // cv::Mat M = cv::Mat(3, 3, CV_64F, m).inv();

    // cv::Mat H(10, 10, CV_64F);
    // for(int i = 0; i < H.rows; i++)
    //   for(int j = 0; j < H.cols; j++)
    //     H.at<double>(i,j)=1./(i+j+1);
    // std::cout << H << '\n';


    // for(int irow=0;irow<3;irow++){
    //   for(int icol=0;icol<3;icol++){
    //     //want to print out each element
    //     std::cout << A.at<double>(irow,icol) << ",";
    //   }//cout-col
    //   std::cout << '\n';
    // }//cout-row
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
