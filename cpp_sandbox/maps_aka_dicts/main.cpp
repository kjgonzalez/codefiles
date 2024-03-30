#include <iostream>
#include <map>
#define nl "\n"

class Rect{public:
    int x;
    Rect(int x_){
        x=x_;
    }
    int area(){return x*x;}
};

void v1(){
    enum Val {red, grn, blu};
    Rect r0(2);
    Rect r1(3);
    Rect r2(5);
    std::map<enum Val, Rect *> d;
    d[red] = &r0;
    d[grn] = &r1;
    d[blu] = &r2;
    printf("val: %d \n",d[blu]->area());
}

void v2(){
    enum Val {red,grn,blu};
    std::map<enum Val, Rect *> d;
    d[red] = new Rect(7);
    d[grn] = new Rect(11);
    d[blu] = new Rect(13);
    printf("val2: %d" nl,d[grn]->area());
    printf("len: %d" nl, (int)d.size());
}

int main(){
    printf("hi\n");
    v2();
    return 0;
}
