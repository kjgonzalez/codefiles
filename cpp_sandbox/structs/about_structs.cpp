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

// METHOD3: different kind of constructor, not yet understood ==================
struct tBox {
  string  type;     // object type as car, pedestrian or cyclist,...
  double   x1;      // left corner
  double   y1;      // top corner
  double   x2;      // right corner
  double   y2;      // bottom corner
  double   alpha;   // image orientation
  tBox (string _type, double _x1,double _y1,
        double _x2,double _y2,double _alpha):
    type(_type),x1(_x1),y1(_y1),x2(_x2),y2(_y2),alpha(_alpha) {}
};
tBox a("car",0,1,2,3,0.5);

printf("%s: %f, %f, %f, %f, %f\n",a.type.c_str(),a.x1,a.y1,a.x2,a.y2,a.alpha);

return 0;
}//main