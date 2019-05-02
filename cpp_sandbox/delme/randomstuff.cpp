/*
Mini sandbox to test things. add / remove as necessary
GUIDELINE: when coming up with a new idea, just make a new function and call it
  in main, which may help preserve older attempts / info
*/

#include <iostream>
#include <vector>
#include <stdio.h>
#include <fstream>

// using namespace std; // include on per-function  basis

void vectorStuff_190502(){
  using namespace std;
  vector<int> a;
  for(int i=0;i<5;i++) a.push_back(i);

  for(int i=0;i<5;i++) printf(" %d",a[i]);
  printf("\n");

}

int main(){
  vectorStuff_190502();
  return 0;
}
