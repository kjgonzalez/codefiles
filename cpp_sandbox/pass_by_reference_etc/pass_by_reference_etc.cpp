/*
will demonstrate examples of passing by various methods, as well as explaining
    differences:
    * pass by value
    * pass by reference
    * pass by pointer
    * pass by definition (as argument)


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
    float area() const {return pi*r*r;} // REQUIRED "const" if you need to pass as const object
    // void addOne() const {r+=1;} // NOT allowed: const function with reassignment
};

float byValue(Circle obj){ // pass args by value
    obj.r +=1;
    return obj.area();
}

float byRef(Circle &obj){ // pass args by reference
    obj.r +=1;
    return obj.area();
}

float byPointer(Circle *obj){ // pass args by pointer
    obj->r +=1;
    return obj->area();
}

float byDefine(const Circle &obj){
    // obj.r +=1; // not allowed if "const"
    // return obj.r*obj.r*pi;
    return obj.area();
}

int main(){
    Circle c(1);
    printf(" r: %f \n area: %f \n", c.r,c.area() );
    cout << "-------------------------" << endl;
    printf("pass by val: %f\n",byValue(c)); // makes a copy of argument
    printf("pass by ref: %f\n",byRef(c));   // modifes reference directly, can't be NULL or changed
    printf("pass by poi: %f\n",byPointer(&c)); // modifies pointer object, may be NULL and changed
    printf("pass by def: %f\n",byDefine(Circle(4)) ); //declare a CONSTANT object as argument
    return 0;
}
