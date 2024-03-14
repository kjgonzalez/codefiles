/*
refresher on C
things to cover: 
* variable - done
* operators - done
* functions - done
* structs - done
* arrays
* memory allocation
* matrix operations? 
* libraries
*/


#include <stdio.h>
#include <math.h> //required for sqrt
#include <stdbool.h> // required for true/false
#include "lib.h"

struct Rect{
    int x;
    int y;
};


float pyt1(float a,float b){ return pow(a*a+b*b,0.5); }
//float pyt1() // polymorphism?
float pyt2(struct Rect r){ // each time you reference Rect, need "struct' in front of it"
    return pow(r.x*r.x+r.y*r.y,0.5);
}


int main() {
    // printf() displays the string inside quotation
    // printf("Hello, World!\n");
    printf("add: %d\n",2+2);
    printf("bool: %d\n",true!=false); 
    printf("char: %c\n",'a');
    printf("str: %s\n","this is a test");
    float res = sqrt(4);
    printf("sqrt: %.2lf\n",res);
    printf("pyt1(3,4): %f\n",pyt1(3,4));
    int x=3;
    int y=4;
    printf("attempt 2: %f\n",pyt1(x,y)); // strangely, this should have thrown an error
    struct Rect r1;
    r1.x = 5;
    r1.y = 12;
    printf("attempt3: %f\n",pyt2(r1));

    // point to function's address
    float (*p_pyt)(float,float) = &pyt1; // point to function's address

    printf("thing:%f\n",(*p_pyt)(1,1));

    printf("simple library: %d\n", add(4,5))







    return 0;
}
