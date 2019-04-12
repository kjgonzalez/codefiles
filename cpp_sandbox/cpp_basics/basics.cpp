/*
author: kris gonzalez
date: 190408
objective: ok, it's clear that you always forget cpp because you dont practice 
    it enough. 

general things to practice: 
* done: for loops
* done: if statements
* done: switch statements
* done: variables
* string operations
    * done: concatenate 2 strings
    * split a string into list/array of strings
    * :x
    * convert string to number
    * convert number to string
    * done: return i'th value
    * done: return substring
    * done: get length of string
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
#include <string> // string class import

#define nl "\n"

int main(){
// part 1: if/else, loops, switches  ===========================================
std::cout << "yo." << nl;
for(int i=0;i<10;i++){
    std::cout << i << " ";
    if(i==0) std::cout << "a ";
    else if(i==1) std::cout << "b ";
    else std::cout << "c ";
    switch(i){
        case (4):
            i+=1;
            std::cout <<"f";
        default:
            std::cout <<"_";
    }//switch
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

// part4: basic string operations ==============================================
/*  * concatenate 2 strings
    * insert string in arbitrary places
    * split a string into list/array of strings
    * convert string to number
    * convert number to string
    * return i'th value */

std::string astr= "this is a test";
astr = astr+". nice.\n";
std::cout << astr;
std::cout << astr.substr(0,3) << nl; // kjg190412: index 3 not incl, like python
int k=astr.find(" a ")+1;
std::cout << k << nl;
//std::cout << astr.length() << nl;
astr = astr.substr(0,k)+"not "+astr.substr(k,astr.length());
std::cout << astr << nl;
}//main

// #include <vector> // keep in mind: THIS IS A VALID PLACE TO PUT STUFF...

//eof

