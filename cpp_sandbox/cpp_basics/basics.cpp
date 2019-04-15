/*
author: kris gonzalez
date: 190408
objective: ok, it's clear that you always forget cpp because you dont practice
    it enough.

HOW TO USE:
g++ -std=c++11 basics.cpp; ./a.out

kjg190412: std flag important for working with modern capabilities (eg. certain
  string operations, etc)

General things to practice:
* done: for loops
* done: if statements
* done: switch statements
* done: variables
* string operations
    * done: concatenate 2 strings
    * done: insert string in arbitrary places
    * done: convert string to number
    * done: convert number to string
    * done: return i'th value
    * done: split a string into list/array of strings
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
#include <stdio.h>  // needed for splitting a string
#include <string.h> // needed for splitting a string

#define nl "\n"

// user-made function to handle splitting a string
std::vector<std::string> split(std::string str,std::string sep){
    char* cstr=const_cast<char*>(str.c_str());
    char* current;
    std::vector<std::string> arr;
    current=strtok(cstr,sep.c_str());
    while(current!=NULL){
        arr.push_back(current);
        current=strtok(NULL,sep.c_str());
    }
    return arr;
}

float pyt(std::vector<float> vec){
  /* example of making a function. return norm2 value of given vector */
  float sum=0;
  for(int i=0;i<vec.size();i++) sum+=pow(vec[i],2);
  return pow(sum,0.5);
}


int main(){

// part 1: if/else, loops, switches  ===========================================
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
//kjg190412: if declare w/o initialize, var can be anything random.
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
/*  * done: concatenate 2 strings
    * done: insert string in arbitrary places
    * done: convert string to number
    * done: convert number to string
    * done: return i'th value
    * done: split a string into list/array of strings
*/

std::string astr= "this is a test"; // initialize
astr = astr+". nice.\n";            // concatenate
std::cout << astr;
std::cout << astr.substr(0,3) << nl; // kjg190412: index 3 not incl, like python
int k=astr.find(" a ")+1;             // find substr in string
astr = astr.substr(0,k)+"not "+astr.substr(k,astr.length()); // insert substr
std::cout << astr << nl;

//convert string to number
std::string bstr = "3.14159";
float bstr_float=std::stof(bstr); // update for c++11
std::cout << bstr_float << nl;
int bstr_int = std::stoi(bstr);
std::cout << bstr_int << nl;

// convert number to string
std::string bstr2 = std::to_string(bstr_float) + " " + std::to_string(bstr_int);
std::cout << "converted back: "+bstr2 << nl;

// return i'th value (entire substrings above)
std::cout << "'a' value: " << astr[astr.find(" a ")+1] << nl;

// no easy way to split a string into substrings, but here's one
std::vector<std::string> arr;
arr=split("This--is--split","--");
for(int i=0;i<arr.size();i++) std::cout << arr[i] << ",";
std::cout << nl;


// part 5: vectors, functions ==================================================
// kjg190412: can be treated a little bit like a list, but only for one type
std::vector<int> v;
v.push_back(0);
v.push_back(1);
for(int i=2;i<5;i++){ v.push_back(i);}
for(int i=0;i<v.size();i++) std::cout << v[i] << " ";
std::cout << nl;

std::vector<float> w;
w.push_back(3);
w.push_back(4);
w.push_back(12);
std::cout << pyt(w) << nl;

// part 6: pointers ============================================================

int var = 3;
int* var_addr = &var; // pointers store addresses, so need '*'

std::cout << "actual value: " << var << nl; // give actual value, using actual variable
std::cout << "memory location: " << &var << nl; // give address, using actual variable
std::cout << "memory location: "<< var_addr << nl; // give addr, using pointer
std::cout << "actual value: " << *var_addr << nl; // give value at address held by pointer
// part 7: classes =============================================================
//kjg190412: normally classes go outside a function, unless only want local scope

/* basics:
    * initialization
    * "deconstruction" ?
    * member variable
    * member function
    * public / private ( / protected ?)
    * inheritance ?
    * super- / sub- classes?
*/

class Rectangle {
    int width, height; // because these not under "public", auto-private
  public:
    Rectangle(int a,int b){
      width=a;height=b;
    }
    void set_wdht (int x,int y){ // can also declare this somewhere else
      width=x;height=y;
    }
    int area (){ return width*height;}
};

// Rectangle::Rectangle(int a,int b){
//   width=a;height=b;
// }

// Rectangle rect;
// rect.set_wdht(3,4);
Rectangle rect(3,4);
std::cout << "area of rect: "<< rect.area() << nl;
}//main

// #include <vector> // keep in mind: THIS IS A VALID PLACE TO PUT STUFF...

//eof
