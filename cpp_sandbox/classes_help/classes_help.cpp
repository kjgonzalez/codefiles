/*
want to cover basic stuff about classes, but put EVERYTHING you can in here.

NOTE:
to compile this:
g++ *.cpp -std=c++11 // don't need cmake, std11 NOT required...

STAT | DESCRIPTION
done | simple class
done | inheritance
done | composition
done | private / protected / public
???? | multiple-inheritance
???? | virtual function

*/
#include <iostream>
#include <string>
using namespace std;

// 01: simple class, nothing fancy
class Shape{
public:
    string color;
    Shape(string color_="black"){color=color_;} // note: this is called a constructor (duh)
    // ~Shape(); // this would be called a destructor, which handles memory
             // deallocation. this is typically automatically handled by c++11
    void set_color(string color_){color=color_;}
};

void fn01_basics(){
    // 01: simple class, nothing fancy
    Shape s;
    s.set_color("pink");
    printf("color: %s \n",s.color.c_str());

}

// 02: inheritance (eg. "a rectangle is a shape")
class Rect:public Shape{
public:
    int height,width;
    Rect(string color_,int height_,int width_):Shape(color_){
        height=height_;width=width_;}
    // if the parent class takes no input arguments, simply do like so:
    // Rect(...){...}
};

void fn02_inheritance(){
    // 02: inheritance
    Rect r("blue",3,4);
    printf("color:%s\n",r.color.c_str());
    printf("height:%i\n",r.height);
    printf("width:%i\n",r.width);
}

// 03: composition
class Fill{
public:
    string fill_color;
    Fill(string fill_color_="lavender"){fill_color=fill_color_;}
};

class Tri{
public:
    int base,height;
    Fill fc;
    Tri(int base_,int height_,string color_="green"):
        base(base_),height(height_),fc( Fill(color_) ){}
};

void fn03_composition(){
    // 03: composition
    Tri t(2,3);
    printf("fill_color:%s\n",t.fc.fill_color.c_str());
    printf("base:%i\n",t.base);
    printf("height:%i\n",t.height);
}

// 04: virtual function
    // a virtual function can be purposely overridden by a derived class, but
    // only really shows value and change when there's an object pointer for the
    // base class that has been derived from.
class Base{ //shape2
public:
    virtual void print(){cout << "printed by base class" << endl;}
    void res(){cout << "base result" << endl;}
};

class Derive:public Base{
public:
    void print(){cout << "printed by derived class" << endl;}
    void res(){cout << "derived result" << endl;}
};

// simple versions, combined: 
// classes, inheritance, composition
class MiniFunc{public:
    MiniFunc() {}; // simple initialization
    int area(int d0, int d1) { return d0 * d1; }
};
class Shape2 {public:
    int identifier;
    Shape2(int id = 3) { identifier = id; }
};
class Rect2:public Shape2{public: // inheritance
    int x, y;
    MiniFunc fn; // composition
    Rect2(int xval,int yval,int id=2){
        x = xval, y = yval, identifier = id;
    }
    int area() { return fn.area(x, y); }
};

void fn04_virtualfns(){
    // 04: virtual function
    Base* pBase; // only really matter when dealing with object pointers
    Derive d;
    pBase=&d;
    pBase->print();
    pBase->res();
}

// 05: using this
class ThisThing{public:
    // "this" keyword is a pointer to class it is within. 
    int a = 3;
    float b=2.4;
    void print(){
        printf("basic: %d\n",a);
        printf("this:  %d\n",this->a);
    }
};//ThisThing


int main(){
    // 05: using this
    ThisThing tt;
    //printf("value: %d\n",tt.a);
    tt.print();
    return 0;
};
