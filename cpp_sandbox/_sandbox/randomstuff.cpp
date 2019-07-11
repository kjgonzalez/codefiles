/*
Mini sandbox to test things. add / remove as necessary
GUIDELINE: when coming up with a new idea, just make a new function and call it
  in main, which may help preserve older attempts / info
*/

#include <iostream>
#include <vector>
#include <stdio.h>
#include <fstream>
#include <math.h>

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

void pyt_anonymous(){
    auto pyt = [](double a, double b, double c){return pow(a*a+b*b+c*c,0.5);};
    printf("ans: %f\n",pyt(3,4,12));
}

int blah(){
    printf(" blah ");
    return 3;
}

void returnToNothing(){
    /* want to know if it's ok t return a value but have it go to nothing.
    answer: yes of course it's ok.
    */
    printf("value: %d\n",blah());
    blah();
    printf("hello world\n");
}

void bufferprint(){
    // kjg190711: want to try and get the same formatting stuff as in printf
    //  also in own strings for fileIO lib
    //note: need <stdio.h>
    printf("Hello world\n");
    printf("Something %d say\n",2);
    char buffer[512];
    sprintf(buffer,"i like to eat %d bananas\n",3);
    printf("%s",buffer);

    sprintf(buffer,"new statement\n");
    printf("%s",buffer);

    sprintf(buffer,"shorter\n");
    printf("%s",buffer);

    sprintf(buffer,"and now way way way way way way longer\n");
    printf("%s",buffer);
    // all this seems to work.

}




int main(){
    bufferprint();

    return 0;
}
