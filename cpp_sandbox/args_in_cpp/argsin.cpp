/*
take in some arguments from the shell, then display them on the screen.


note: in current implementation...
compile: g++ argsin.cpp -o test
run: ./test arg1 arg2 ...

source:
https://www.geeksforgeeks.org/command-line-arguments-in-c-cpp/
*/

#include <iostream>
using namespace std;

int main(int argc, char **argv){ //this line is key
  cout << "hello world" << endl;

  // how to call each argument given.
  // NOTE: arg[0] is the program name, e.g. "./a.out"
  cout << "you've given "<<argc<<" arguments:\n";
  for (int i=0;i<argc;i++){
    cout << ">> " << argv[i] << endl;
  }//forloop

  return 0;
}//int main
