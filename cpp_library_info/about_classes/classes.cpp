/*
basics of classes

notes: 
* private: ("access specifier") cannot be accessed nor viewed outside the class
* protected: cannot be accessed outside the class, but can be inherited
* public: can be accessed and modified from outside the class
* inheritance: "X is a Y" (human is a person)
* composition: "Y has an X" (a person has a name / height / weight)
* struct: originally part of C. in C++, all attributes and methods are public (note: in C, structs 
    cannot contain methods), making them nearly identical to a class, which has all att's/methods 
    private by default.
*/

#include <stdio.h> // only for printf

//basic struct
struct Person{
    unsigned char age;
    unsigned char height_cm;
};

// basic class: 
class Rect {
// by default, all members and methods are private
private:
    int color;
protected:
    int x,y; // can be used by a child class: square
public:
    Rect(int xval = 0, int yval = 0) { x = xval; y = yval; color = 3; }
    int area() { return x * y; }
};

// basic inheritance
class Square:public Rect{
public:
    Square(int xval = 0) { x = xval; y = xval; }
};

// basic composition
class Material{
public:
    int mat_num;
    Material(int material_number = 2) { mat_num = material_number; }
};

class Triangle {
public:
    int x, y;
    Material mat;
    Triangle(int xval, int yval) { x = xval; y = yval; mat.mat_num = 3; }
};

int main() {
    printf("hi\n");

    Rect r(2, 3);
    printf("rect area: %d \n", r.area());

    Triangle tri(3, 4);
    printf("tri mat: %d \n", tri.mat.mat_num);

    return 0;
}
