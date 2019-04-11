/*
author: kris gonzalez
date: 190408
objective: ok, it's clear that you always forget cpp because you dont practice 
    it enough. 

general things to practice: 
* for loops
* if statements
* switch statements
* variables
* string operations
* vectors
* make mask / alternate reference for function (eg. inv=np.linalg.inv)
* sprintf / a convenient way to print
* simple powerful way to use arrays (eigen?)
* matrix operations
* some basic ai package???


stuff to practice for classes:
* initialization
* declaring
* methods
* attributes
* class vars?
* private / public items
* ???

*/

#include <iostream>
#include <vector> // only needed for certain things
#include <math.h> // required for pow()

#define nl "\n"

int main(){
// part 1: if/else & loops =====================================================
std::cout << "yo." << nl;
for(int i=0;i<5;i++){
    std::cout << i << " ";
    if(i==0) std::cout << "a ";
    else if(i==1) std::cout << "b ";
    else std::cout << "c ";
} // forloop
std::cout << nl;

// part2: variables ============================================================
int a=3,b=8;
float c;
c=3;
char d='a';
char e[]="test";
// kjg190411: need to include that const char * thing at some point too
std::cout << a << b << c << d << e<< nl;

// part3: basic math operations ================================================
std::cout << "add, sub " << a+b-3 << nl;
std::cout << "mult, div " << 2*c/5 << nl;
std::cout << "power " << pow(2,3) << nl;
std::cout << "modulus " << b%a << nl;

}//main

// #include <vector> // keep in mind: THIS IS A VALID PLACE TO PUT STUFF...

//eof

