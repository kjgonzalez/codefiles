/*
author: Kris Gonzalez
date: 190417
objective: simple examples of eigen (to show similarity to numpy)
alright, so you'ld like to practice eigen so you know how to do matrix 
    operations in the future. let's get on that. however, let's try and have a 
    project in mind so that it has immediate applicability... eh? you know 
    what? maybe you could do something cool with the rpi or the arduino. the 
    only real argument for you doing something in c++ is for restricted 
    hardware (let's be honest here).

Things to test out: 
  * initializing a matrix
  * converting tuypes in a matrix
  * matrix multiplication
  * element-by-element multiplication
  * getting inverse of matrix
  * selecting a subarray of a matrix
  * loading a matrix from a file
  * saving a matrix to a file
  * saving a matrix in a binary file (eigen native format???)
  * do a row stack & column stack
  * 
*/

#include <iostream>
#include <Eigen/Dense>
// using Eigen::MatrixXd; //will not use this for now

int main(){

std::cout << "hello world" << std:: endl;

// initialize a matrix variable
Eigen::MatrixXd m(2,2); //if not including eigen in namespace

// quickly assign values to matrix
// NOTE: you can fill up blocks of a matrix like this as well (e.g. put a 2x2 in a 2x2 region of a larger matrix)
m << 1,2,
     3,4;

std::cout << "matrix:\n" << m << "\n";

}//main



//eof

