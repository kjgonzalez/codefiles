/*
date: 200206
objective: describe the various forms of functions that cpp can run, as well as
how they are created

STAT | DESCRIPTION
done | normal, defined at top
done | normal, defined at bottom
done | lambda (requires c++11)
done | inline function (speed vs size)

*/


#include <iostream>
using namespace std;

int add1(int x){
    return x+1;
}

int add2(int x);

inline int add4(int x){
    return x+4;
}

int main(){
    printf("Various function definitions / uses\n");
    cout << "01: normal, defined at top: " << add1(0) << endl;
    cout << "02: normal, defined at bot: " << add2(0) << endl;

    auto add3 = [](int x){return x+3;};
    cout << "03: lambda function: " << add3(0) << endl;

    cout << "04: inline function (program speed vs size): "<<add4(0) << endl;
    return 0;
}

int add2(int x){
    return x+2;
}
