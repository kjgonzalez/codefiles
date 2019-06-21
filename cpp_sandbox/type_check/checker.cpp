/*
author: kris gonzalez
date: 190521
objective: have an overloaded function be able to return the type of a variable.
*/

#include <iostream>
#include <vector>
#include <string.h>
#include "typecheck.h"

int main(){
    float a=1.5;
    double b=1.6;
    std::string s="yes";

    printf("Type Checker:\n");
    printf("type: %s\n",gettype(false).c_str());
    printf("type: %s\n",gettype(1).c_str());
    printf("type: %s\n",gettype(a).c_str());
    printf("type: %s\n",gettype(b).c_str());
    printf("type: %s\n",gettype('a').c_str());
    printf("type: %s\n",gettype(s).c_str());

    printf("\n");
    return 0;
}
