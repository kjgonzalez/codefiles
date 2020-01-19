/*
date: 200118
objective: create the game snake, in cpp. for the moment, GUI will be in opencv. later may want to use Qt libraries

GENERAL ISSUES / OBJECTIVES
STAT | DESCRIPTION
???? | initialize basic libraries, keyboard control
???? | create game board (10x10 grid)
???? | create "snake" object as single block
???? | be able to move snake with WASD
???? | create "apple" object
???? | create "auto-move" behavior (snake is always moving)
???? | create "eating" behavior (head of snake occupies apple location)
???? | create "growing" behavior (snake length increases when eating an apple)
???? | BONUS: include eigen library?
*/

#include <iostream>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <random>
#include <gainput/gainput.h>


using namespace std;

int main() {
    // basic initialization
    cv::VideoCapture stream1(0);   //0 is the id of video device.0 if you have only one camera.
    
    if (!stream1.isOpened()) { //check if video device has been initialised
    cout << "cannot open camera";
    } //if_statement

    //unconditional loop
    while (true) {
    cv::Mat cameraFrame;
    stream1.read(cameraFrame);
    cv::imshow("cam", cameraFrame);
    if (cv::waitKey(30) >= 0)
    break;
    } //mainloop
    return 0;
} //main
