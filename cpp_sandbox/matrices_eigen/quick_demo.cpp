/*
author: Kris Gonzalez
date: 190416
objective: want to do a quick test using eigen library for matrices. using start example from below
source: https://eigen.tuxfamily.org/dox/GettingStarted.html

HOW TO COMPILE:
    g++ -std=c++11 -I C:\Users\kris\repos\eigen-git-mirror\ .\quick_demo.cpp
*/

#include <iostream>
#include <Eigen/Dense>
using Eigen::MatrixXd;
int main()
{
  MatrixXd m(2,2);
  m(0,0) = 3;
  m(1,0) = 2.5;
  m(0,1) = -1;
  m(1,1) = m(1,0) + m(0,1);
  std::cout << m << std::endl;
}
