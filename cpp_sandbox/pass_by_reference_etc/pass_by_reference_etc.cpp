/*
will demonstrate examples of passing by various methods, as well as explaining
    differences:
    * pass by value
    * pass by reference
    * pass by pointer


*/

#include <iostream>
#define pi 3.14159
using namespace std;

class Circle{
public:
    // member variables
    float r;

    // member functions
    Circle(float r_){r=r_;}
    float area(){return pi*r*r;}
};

float byValue(Circle obj, Circle obj2){ // pass args by value
    obj.r +=1;
    return obj.area();
}

float byRef(Circle &obj,Circle &obj2){ // pass args by reference
    obj.r +=1;
    return obj.area();
}

float byPointer(Circle *obj, Circle *obj2){ // pass args by pointer
    obj->r +=1;
    obj2 = obj;
    cout << "obj2 radius: " << obj2->r << endl;
    return obj->area();
}


int main(){
    Circle c(1);
    printf(" r: %f \n area: %f \n", c.r,c.area() );
    cout << "-------------------------" << endl;
    printf("area, pass by val: %f\n",byValue(c,c)); // makes a copy of argument
    printf("area, pass by ref: %f\n",byRef(c, c ));   // modifes reference directly, can't be NULL or changed
    printf("area, pass by poi: %f\n",byPointer(&c, NULL)); // modifies pointer object, may be NULL and changed


    return 0;
}
