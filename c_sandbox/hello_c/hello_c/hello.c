/*
refresher on C
things to cover:
* variable - done
* operators - done
* functions - done
* structs - done
* arrays
* memory allocation
* matrix operations? - oof...
* libraries - done
* is there polymorphism? not really
* 
* 
* 
*/


#include <stdio.h>
#include <math.h> //required for sqrt
#include <stdbool.h> // required for true/false
#include "lib.h"

void print(char* strarr) {
    // make life easier, automatically add a newline after each print statement
    printf(strarr);
    printf("\n");
}

struct Rect {
    int x;
    int y;
    int init;// = false;
    int (*rect_area)(struct Rect r);

};

int fn_rect_area(struct Rect r) {
    return r.x * r.y;
}
void rect_init(struct Rect r, int x0, int y0) {
    // does init need to be called last?
    r.x = x0;
    r.y = y0;
    r.rect_area = &fn_rect_area;
    print("done");
}



float pyt1(float a, float b) { return pow(a * a + b * b, 0.5); }
//float pyt1() // polymorphism?
float pyt2(struct Rect r) { // each time you reference Rect, need "struct' in front of it"
    return pow(r.x * r.x + r.y * r.y, 0.5);
}

void vars_and_functions() {
    printf("add: %d\n", 2 + 2);
    printf("bool: %d\n", true != false);
    printf("char: %c\n", 'a');
    printf("str: %s\n", "this is a test");
    float res = sqrt(4);
    printf("sqrt: %.2lf\n", res);
    printf("pyt1(3,4): %f\n", pyt1(3, 4));
    int x = 3;
    int y = 4;
    printf("attempt 2: %f\n", pyt1(x, y)); // strangely, this should have thrown an error
    struct Rect r1;
    r1.x = 5;
    r1.y = 12;
    printf("attempt3: %f\n", pyt2(r1));
    // point to function's address
    float (*p_pyt)(float, float) = &pyt1; // point to function's address
    printf("thing:%f\n", (*p_pyt)(1, 1));
    printf("simple library: %d\n", add(4, 5));
}


float len_arr(int array[]) {
    print("sz0: %d", sizeof(array));
    print("sz1: %d", sizeof(array[0]));
    print("%d", array[0]);
    print("%d", array[1]);
    print("%d", array[2]);
    //print("%d", sizeof(array));
    //return ((float)sizeof(array)) / (float)sizeof(array[0]);
    return -1;
}

void arrays() {
    // goal is to play around with arrays a little bit
    print("arrays -------------------");
    int arr0[] = { 7,8,9 };
    print("first value: %d", arr0[0]);
    print("test");
    print("sz_top %d", sizeof(arr0));
    print("size: %d", sizeof(arr0)/sizeof(arr0[0]));
    print("size2:%d", len_arr(arr0));
}

struct Rect *Rect_init(int x0, int y0) {
    struct Rect rect;
    rect.x = x0;
    rect.y = y0;
    rect.rect_area = &fn_rect_area;
    return &rect;
}

int main() {
    // printf() displays the string inside quotation
    // printf("Hello, World!\n");
    //vars_and_functions();
    //arrays();
    //struct Rect r1;
    //r1.x = 2;
    //r1.y = 3;
    //r1.rect_area = &fn_rect_area;

    //rect_init(r1, 2, 3);
    struct Rect* r1;
    r1 = Rect_init(3, 4);

    print("area: %d",r1->rect_area(*r1));


    return 0;
}