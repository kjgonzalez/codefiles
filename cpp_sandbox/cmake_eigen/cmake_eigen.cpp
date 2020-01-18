/*
author: Kris Gonzalez
date: 200118
objective: use eigen library, but compile using cmake. proof of concept to ensure this works.

src1: https://eigen.tuxfamily.org/dox/GettingStarted.html
src2: https://eigen.tuxfamily.org/dox/TopicCMakeGuide.html
KJG200118: get eigen by cloning this repo: https://gitlab.com/libeigen/eigen

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
