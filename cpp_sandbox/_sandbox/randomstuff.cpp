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

void vectorStuff(){
  // created 190502
  using namespace std;
  vector<int> a;
  for(int i=0;i<5;i++) a.push_back(i);

  for(int i=0;i<5;i++) printf(" %d",a[i]);
  printf("\n");

}

void vectorArray(){
  // created 190502
  // objective: test out an "array of vectors of ints"
  using namespace std;
  vector<int> x[3];
  x[0].push_back(0);
  x[1].push_back(1);
  x[1].push_back(2);
  x[2].push_back(3);
  x[2].push_back(4);
  x[2].push_back(5);
  for(int ArrIndex=0;ArrIndex<3;ArrIndex++){
    for(int VectIndex=0;VectIndex<x[ArrIndex].size();VectIndex++) {
      cout << x[ArrIndex][VectIndex]<< " ";
      }
    printf("\n");
    }
}


int main(){
  vectorArray();
  return 0;
}
