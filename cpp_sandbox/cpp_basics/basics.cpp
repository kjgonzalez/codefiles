/*
author: kris gonzalez
date: 190408
objective: simple review of cpp basics

HOW TO USE:
g++ -std=c++11 basics.cpp; ./a.out

kjg190412: std flag important for working with modern capabilities (eg. certain
  string operations, etc)

General things to practice:

1  printing to screen & basic math operations
     1.1 cout / printf
     1.2 +,-,*,/,pow,mod
     1.3 system-level commands
2  if/else, loops, switches
3  variables
   int, float, char, enum, struct
4  string operations
5  vectors & functions
     5.1 vectors
     5.2 functions
     5.3 anonymous functions
6  file I/O
7  pointers
8  classes
9  matrices



* done: for loops
* done: if statements
* done: switch statements
* done: variables
* done: string operations
    * done: concatenate 2 strings
    * done: insert string in arbitrary places
    * done: convert string to number
    * done: convert number to string
    * done: return i'th value
    * done: split a string into list/array of strings
* done: structs
* done: vectors
* done: because of strict typing, how to convert between different var types
    * done: i to f, f to i
    * done: str to f/i, f/i to str
    * done: how to use static character strings (see below)
    * done: this: https://www.geeksforgeeks.org/difference-const-char-p-char-const-p-const-char-const-p/
* make mask / alternate reference for function (eg. inv=np.linalg.inv)
* done: printf / a convenient way to print
* inline functions
* pointers
* calling a function as an argument to another function?

* simple powerful way to use arrays (eigen?)
* matrix operations
* some basic ai package???
* done: how to import / use another library / external cpp file (to help break up a
    file into multiple parts). kjg19502: see "separate_compilation/"
* done: basic file i/o
* stuff to practice for classes / objects:
    * done: initialization
    * done: declaring
    * done: methods
    * done: attributes
    * class vars?
    * done: private / public items
    * inheritance

* small case study:
    1. have a csv file to read from, with header row
    2. load file into memory, parse into a matrix
    4. do some small operations on data
    3. plot the data on a graph (apparently hard to do?)


*/

#include <iostream>
#include <vector> // only needed for certain things
#include <math.h> // required for pow()
#include <string> // string class import
#include <stdio.h>  // needed for splitting a string & sometimes I/O operations
#include <string.h> // needed for splitting a string
#include <fstream> // I/O operations

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
} //fn split

float pyt(std::vector<float> vec){
  /* example of making a function. return norm2 value of given vector */
  float sum=0;
  for(int i=0;i<vec.size();i++) sum+=pow(vec[i],2);
  return pow(sum,0.5);
} //fn pyt

// std::string rpad(std::string inp, int maxLength){
//     /* pad right side of a given string with given character to given length */
//     if(maxLength>inp.size()) inp.insert(maxLength - inp.size(),maxLength,'=');
//     return inp;
// }//rpad

std::string rpad(std::string str,int maxLength=70,const char& filler = '='){
    if(maxLength>str.size()) str.insert(str.size(),maxLength-str.size(),filler);
    return str;
}//rpad

std::string lpad(std::string str,int maxLength=70,const char& filler = '='){
    if(maxLength>str.size()) str.insert(0,maxLength-str.size(),filler);
    return str;
}//lpad


int main(){

// 1  printing to screen & basic math operations ===============================
printf("%s\n",rpad("= 1: printing to screen & basic math operations").c_str());

// want to have simple way to print to screen
int zz=5;
std::cout << "method 1, with cout. var: " << zz << nl;
printf("method 2, with printf. var: %d\n",zz); //kjg190415: this is convenient

std::string sampleString= "sampleString";
std::cout << "method1: "<<sampleString << std::endl;
printf("method2: %s\n",sampleString.c_str());

/* PARAMETERS FOR PRINTF. src: http://www.cplusplus.com/reference/cstdio/printf/
  SYM  DESCRIPTION                                  EXAMPLE
  d/i Signed decimal integer                        392
  u   Unsigned decimal integer                      7235
  o   Unsigned octal                                610
  x   Unsigned hexadecimal integer                  7fa
  X   Unsigned hexadecimal integer (uppercase)      7FA
  f   Decimal floating point, lowercase             392.65
  F   Decimal floating point, uppercase             392.65
  e   sci notation (mantissa/exponent), lowercase   3.9265e+2
  E   sci notation (mantissa/exponent), uppercase   3.9265E+2
  g   Use the shortest representation: %e or %f     392.65
  G   Use the shortest representation: %E or %F     392.65
  a   Hexadecimal floating point, lowercase         -0xc.90fep-2
  A   Hexadecimal floating point, uppercase         -0XC.90FEP-2
  c   Character                                     a
  s   String of characters                          sample
  p   Pointer address                               b8000000
  n   Nothing printed. arg is pointer to signed int (empty??)
  %   %% will write a single % to the stream.       %
*/

printf("%s\n",rpad("= 1.2: basic math operations ",60).c_str());
// 1.2 basic math operations
std::cout << "add, sub " << 4+5-3 << nl;
std::cout << "mult, div " << 2*10.1/5 << nl;
std::cout << "power " << pow(2,3) << nl;
std::cout << "modulus " << 8%3 << nl;

//1.3 system operations
system("echo system level commands are also possible like so.");



// part 2: if/else, loops, switches  ===========================================
printf("%s\n",rpad("= 2: if/else, loops, switches ").c_str());

printf("forloop: ");
for(int i=0;i<10;i++){
    printf("%d ",i);
    }
printf(nl);

printf("do-while & while loop: ");
int icounter=0;
do {printf("%d ",icounter);icounter++;
    } while(icounter <6);
while(icounter<8){printf("%d ",icounter);icounter++;
    }
printf(nl);

printf("if/else: ");
int ifvar=3;
if(ifvar==0) printf("this one");
else if(ifvar==1) printf("that one");
else printf("the other one");
printf(nl);



printf("switches: ");
switch(ifvar){
    case(0):
        printf("yeehaw");break;
    case(3):
        printf("howdy");break;
    default:
        printf("giddyup");break;
    } //switch
printf(nl);



// part 3: variables ===========================================================
printf("%s\n",rpad("= 3: variables (int, float, ...) ").c_str());
//kjg190412: if declare w/o initialize, var can be anything random.
int a=3,b=8;
float c;
c=3;
char d='a';
char e[]="test";
// kjg190411: need to include that const char * thing at some point too
std::cout << a << b << c << d << e<< nl;

// want to show how to convert between various methods. can be explicit or implicit

// int <> float //kjgnote: will only consider "int" (4bytes/32bits,signed)
// int <> double
// float <> double
int x_int=5;
float x_flt=static_cast<float>(x_int);
float x_flt2=x_int+0.0; // implicit conversion to float / double
// for brevity, will omit other combinations. however, use above as template.

// will try an enumerator, per ...
// https://en.cppreference.com/w/cpp/language/enum
enum Color {red,green,blue=5}; //note: can't then use something like "yellow"
// default values: red=0, green=1, blue=2, etc (must be some kind of int)

Color cc = red;
switch(cc){
  case red  : printf("red, %d\n",cc);  break;
  case green: printf("green, %d\n",cc);break;
  case blue : printf("blue, %d\n",cc); break;
}

struct Dog{
    int age;
    std::string name;
};
auto printDogInfo = [](Dog dog) {
    /* anonymous function, explained below */
    printf("dog name: %s\n",dog.name.c_str());
    printf("dog age : %d\n",dog.age);
};

Dog woofer;
woofer.age=3;
woofer.name = "woof";
printDogInfo(woofer);

// part 4: basic string operations =============================================
printf("%s\n",rpad("= 4: string operations ").c_str());

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

// part 6: vectors, functions, anonymous functions =============================
printf("%s\n",rpad("= Vectors & Functions ").c_str());

// 5.1 vectors
// kjg190415: need examples of more member functions
std::vector<int> v;
v.push_back(0);
v.push_back(1);
for(int i=2;i<5;i++){ v.push_back(i);}
for(int i=0;i<v.size();i++) std::cout << v[i] << " ";
std::cout << nl;

// 5.2 functions
std::vector<float> w;
w.push_back(3);
w.push_back(4);
w.push_back(12);
std::cout << pyt(w) << nl;

// 5.3 anonymous functions (lambda functions)
auto firstLambda = [](int a, int b) {return a+b;};
std::cout << firstLambda(3,4) << "\n";

std::vector<bool> values(3,false);
values[1]=true;

auto print3 = [](std::vector<bool> vec){std::cout<<vec[0]<<" "<<vec[1]<<" "<<vec[2]<<"\n";};

print3(values);



// part 7: file i/o ============================================================
printf("%s\n",rpad("= 7: File I/O ").c_str());
/* File i/o is disappointingly tricky. There's one style to do it for writing to
    a file, and another style to read from a file. the best way of each is given
    below. note: you need <fstream> for reading and <stdio.h> for writing.
*/
// printf("METHOD fstream: writing to file... ");
// std::ofstream f_out;
// f_out.open("file.txt");
// f_out << "Line 1" << nl;
// f_out << "Line " << 2 << nl;
// f_out.close();
// printf("done.\n");

printf("METHOD cstdio/stdio.h: writing to file... ");
FILE *f_out2=fopen("file.txt","w");
fprintf(f_out2,"new line 1\n");
fprintf(f_out2,"new line %d\n",2);


printf("method with fstream: reading from file... \n");
std::ifstream fin("file.txt");
std::vector<std::string> raw;
std::string line;
while(!fin.eof()){
    getline(fin,line);
    raw.push_back(line);
    }
fin.close();

printf("file contents:\n");
for(int i=0;i<raw.size();i++){
  printf("%s\n",raw[i].c_str());
}

system("rm file.txt");

// part 7: pointers ============================================================
printf("%s\n",rpad("= 7: Pointers ").c_str());

int var = 3;
int* var_addr = &var; // pointers store addresses, so need '*'

std::cout << "actual value: " << var << nl; // give actual value, using actual variable
std::cout << "memory location: " << &var << nl; // give address, using actual variable
std::cout << "memory location: "<< var_addr << nl; // give addr, using pointer
std::cout << "actual value: " << *var_addr << nl; // give value at address held by pointer

//arrow operator allows access to the members of an object that a pointer is pointing to.
std::string someString = "this text is accessed via a pointer.";
std::string* delme = &someString;
printf("%s\n",delme->c_str());


// part 8: classes =============================================================
printf("%s\n",rpad("= 8: Classes & Objects ").c_str());
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


Rectangle rect(3,4);
printf("area of rect: %f\n", static_cast<float>(rect.area()) );
std::cout << "area of rect: "<< rect.area() << nl;

}//main

//eof
