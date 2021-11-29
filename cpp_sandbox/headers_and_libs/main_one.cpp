/*
here, want to create a function and a class. then,
  want to move it over to another file that will be a header

KJGNOTE: how to compile for standard 11: g++ -std=c++11 main_one.cpp norms.cpp

KJGNOTE: sometimes, get error as below:
    warning: ISO C++ forbids converting a string constant to ‘char*’ [-Wwrite-strings]
MatrixXd m(2,2);
in order to fix, use "char const *", not "char *":
    char const *name; // KJGNOTE: THIS IS THE PROPER WAY TO DEAL WITH STRINGS
ADDITIONALLY, able to still rename just like in a string.

kjg190502: need to include all relevant cpp files in compilation command (see above)
*/

#include <iostream>
#include <math.h>
#include <vector>
#include "rectangle.h"
#include "norms.h"
#define nl "\n"

class puppy{
  public:
    int age;
    char const *name; // KJGNOTE: THIS IS THE PROPER WAY TO DEAL WITH STRINGS
    // warning: ISO C++ forbids converting a string constant to ‘char*’ [-Wwrite-strings]
    puppy(int a,char const *b){
      age=a;
      name = b;
    }//constructor
    void grow(){
      std::cout << "puppy ages by one year: "<<++age<< nl;
    }//void age
    void bark(){
      std::cout << name << " barks!" << nl;
    }//void bark
  // public section
};  //class puppy

//KJGNOTE: the following two pieces of code aren't needed here, they've been
//  moved to norms.cpp/h and rectangle.h

// double pyt(double a, double b){
  // return pow(a*a+b*b,0.5);
// } //pyt

// class rect{
// public:
//   int ht,wd;
//     rect(int height,int width){
//       ht=height;
//       wd=width;
//     }//constructor
//     int area(){
//       return ht*wd;
//     }//void area
//     int perim(){
//       return 2*(ht+wd);
//     }//void perim
// }; //class rect


int main(){
  // std::vector<double> v;
  std::vector<double> v = {1,2,3};
  // v = ,2,3];
  std::cout << "test: "<< pyt(3,5) << nl;
  std::cout << "vector length: " << v.size() << nl;

  // puppy class
  puppy pup(3,"Sparky");
  std::cout << "pup age: " << pup.age << nl;
  std::cout << "pup name: " << pup.name << nl;
  pup.name = "Bowie";
  pup.grow();
  pup.bark();

  // rect class
  rect adam(3,4);
  std::cout << "area: " << adam.area() << nl;
  std::cout << "perimeter: " << adam.perim() << nl;

  return 0;
} //main
