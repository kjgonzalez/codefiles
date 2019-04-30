/*
just want to practice structs for a moment to get a good understanding about them.

how to compile: 
g++ -std=c++11 about_structs.cpp
*/

#include <iostream>
using namespace std;

int main(){

// METHOD1: Create the struct, declare it, add variables. ======================
struct Dog{
    int age; //years
    int height; //cm
}; //struct dog

auto printAgeHeight= [](int age, int height) {
    printf("age: %d\n",age);
    printf("height: %d\n",height);
    };

Dog lassie;
lassie.age=3; //years
lassie.height=50; //cm
printf("Dog info:\n");
printAgeHeight(lassie.age,lassie.height);


// METHOD2: Create the struct with a constructor ===============================
struct Cat{
    int age;
    int height;
    Cat(int ageValue,int heightValue){
        age=ageValue;
        height=heightValue;
    }
};//struct cat

Cat meow(7,40);
printf("Cat info:\n");
printAgeHeight(meow.age,meow.height);




return 0;
}//main