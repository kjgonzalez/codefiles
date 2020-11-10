/*
This file covers basics about using eigen such as initializing a matrix, operations, and functions.

How to Install / Use Eigen: 
1. go to desired install folder
2. git clone https://gitlab.com/libeigen/eigen
3. add path/to/eigen to include directories: Project >> PROJECT Properties >> 
    VC++ Directories >> Include Directories >> (add path here)
4. start using Eigen

things to add: 
  * append new row(s)
  * append new col(s)

*/

#include <iostream>
#include <Eigen/Dense>
using namespace std;
int main() {
  namespace eig = Eigen;
  // create a matrix: can either be a dynamic or static matrix:

  //dynamic matrix (note the "X" in the name)
  eig::MatrixX<double> x1(2, 2);
  x1 << 0, 1, 2, 3;

  // static matrix (note the delimiting of dimensions in the template)
  eig::Matrix<double, 2, 2> x2;
  x2 << 5,2,3,1;
  
  eig::MatrixX<double> x3(2, 5);
  x3 << 0, 1, 2, 3, 4, 5, 6, 7, 8, 9;

  // alternative to matrices are arrays, which function a little bit more like numpy arrays
  eig::ArrayXX<double> y1(2, 2); // having two 'X's is correct
  y1 << 2, 3, 4, 5;
  eig::Array<double, 2, 2> y2; // also has a static option
  y2 << 5, 6, 7, 8;

  // conversion between the two: 
  eig::MatrixX<double> xtemp = y1.matrix();

  // note there are also vectors, but used to a far lesser extent
  eig::Vector3<double> v;
  v << 1, 2, 3, 4, 5, 6;

  // basic per-element operations: 
  cout << "scalar addition \n" << (x1.array() + 10).matrix() << endl; // note: need to be in array
  cout << "scalar subtraction \n" << (x1.array() - 10).matrix() << endl;
  cout << "scalar multiplication \n" << x1 * 10 << endl;
  cout << "scalar division \n" << x1 / 10 << endl;
  
  // matrix operations
  cout << "matrix addition \n" << x1 + x2 << endl;
  cout << "matrix subtraction \n" << x1 - x2 << endl;
  cout << "transpose \n" << x1.transpose() << endl;
  cout << "inverse \n" << x1.inverse() << endl;
  cout << "matmult \n" << x1 * x2 << endl;
  cout << "conjugation \n" << x1.conjugate() << endl;

  // WARNING: AVOID TRANSPOSITION ISSUES, WHICH OCCUR WHEN TRANSPOSING IN-PLACE:
  // a=a.transpose() // DO NOT DO THIS
  x1.transposeInPlace();
  x1.transposeInPlace();

  // arithmetic reduction operations:
  cout << "sum the matrix: " << x1.sum() << endl;
  cout << "mult the matrix: " << x1.prod() << endl;
  cout << "matrix mean: " << x1.mean() << endl;
  cout << "matrix min: " << x1.minCoeff() << endl;
  cout << "matrix max: " << x1.maxCoeff() << endl;
  
  // matrix properties
  cout << "diagonal: " << x1.diagonal().transpose() << endl;
  cout << "shape (should be 2,5): " << x3.rows() << ',' << x3.cols() << endl;
  
  // matrix manipulation
  eig::Map < eig::MatrixX<double>> x4(x1.data(), 1,x1.size());
  cout << "reshape: " << x4 << endl;
  // append a row
  eig::MatrixX<double> x6(2,2);
  x6 << 0, 1, 2, 3;
  x6.conservativeResize(x6.cols() + 1, eig::NoChange); // shortcut
  x6(2, 0) = 5;
  x6(2, 1) = 6;
  cout << "append row: \n" << x6 << endl;

  // taking part of matrix: 
  eig::MatrixX<double> x5(5, 5);
  for (int i = 0; i < x5.size(); i++) x5(i) = i;
  cout << "initial \n" << x5 << endl;

  cout << "arbitrary block \n" << x5.block(1, 1, 2, 2) << endl;
  cout << "column1 \n" << x5.block(0, 1, x5.rows(), 1) << endl;
  cout << "row3 \n" << x5.block(3, 0, 1,x5.cols()) << endl;

  // special matrices. only static, can be whatever dimensions needed
  cout << "identity matrix \n" << eig::Matrix<double,3,3>::Identity() << endl;
  cout << "zeros \n" << eig::Matrix<double, 3, 3>::Zero() << endl;
  cout << "ones\n" << eig::Matrix<double, 3, 3>::Ones() << endl;



}




