/*
refresher on C
things to cover:
01. types     - done1
02. operators - done1
03. functions - done1
04. structs   - done1
05. arrays    - done1
06. libraries - done
07. memory allocation
08. preprocessor commands
09. file i/o

formatting printf: https://cplusplus.com/reference/cstdio/printf/
cheatsheet: d, u, f, x, z*, l*, c, s, p
*/


#include <stdio.h> // required for 
#include <math.h> //required for sqrt & pow
//#include <stdbool.h> // required for true/false
#include "lib.h"

typedef int err_t; // can define own types
void p01_types() {
    // note: can put "unsigned" before any integer and get the unsigned version
    int* ptr = NULL;
    int arr[10];
    char* cstring = "this is a c-string"; // auto-null terminated
    union Combined { // union: multiple types access same memory
        unsigned int val;
        char bytes[4];
    } cc;
    cc.val = 12;
    union Combined d = { 930 };
    printf("- 01 variables --------------\n");;
    printf("char      sz:%zu\n", sizeof(char));      // nbytes: 1
    printf("short     sz:%zu\n", sizeof(short));     // 2
    printf("int       sz:%zu\n", sizeof(int));       // 4
    printf("long      sz:%zu\n", sizeof(long));      // 4
    printf("long long sz:%zu\n", sizeof(long long)); // 8
    printf("float     sz:%zu\n", sizeof(float));     // 4
    printf("double    sz:%zu\n", sizeof(double));    // 8
    printf("ptr       sz:%zu\n", sizeof(ptr));      // address, 8 bytes  (64bit machine)
    printf("arr-all   sz:%zu\n", sizeof(arr));      // if known array, whole range. 40 bytes
    printf("arr-ptr   sz:%zu\n", sizeof(&arr));     // address, 8 bytes
    //note: bool not builtin, would need <stdbool.h>
    printf("%s\n", cstring);
    printf("union     sz:%zu\n", sizeof(cc));
}

void p02_operators() {
    printf("- 02 operators --------------\n");
    (1 + 1) * 6 / 2 - (3 % 2); // arithmetic operators (note: '%'== modulo). 
    // note: i++, ++i, i--, --i (unary value change, not recommended)
    1 > 0;  // relational operators: >, <, >=, <=, !=, == (true/false via <stdbool.h>)
    !0;     // logical operators (note: non-zero == 1 == true): !, &&, ||
    1 << 3; // binary operators: &, |, ^(xor), ~(1's complement), <<(left shift), >>(right shift)

    int i = 0;
    i += 3; // assignment operators: =, += (or replace'+' with - * / % << >> & ^ or |)

    // pointers & misc
    int* p_int; // "integer pointer"
    p_int = &i; // "address of"
    int j = *p_int; // "value at" (note: '*' right of '=')
    // note: x->var for members of struct pointers
    printf("%d, %p, %d\n", i, p_int, j);
    sizeof(double); // sizeof: return size of item in bytes
    int k[] = { 1,2,3 }; // array [] & assignment {}
    int a = i > 1 ? 3 : -1; // ternary operator: (expr) ? if_true : if_false
    // note: exponents are not built-in, but require <math.h> to run: 
    double power3 = pow(2, 3);
}


int fn_example(int pass_by_val, int* pass_by_pointer)
{   // note: no pass by reference in c
    return pass_by_val + *pass_by_pointer;
}
err_t fn_typical(int* out_param, int in_param)
{
    /* This is 'typical' structure of more complex c programs: 
        * the returned value is an error. 0=OK, !0=some error
        * an "output parameter" is where the user gives a pre-allocated 
            variable to modify in the function
        * other parameters are given after the out params
    */
    *out_param = in_param * 3;
    if (*out_param < 10) return 0;
    else return 1; 
}
void fn_define_later(); // can be defined later, but used immediately
struct Cyl{int r;int h;};
struct Cyl tmp() { struct Cyl c; c.r = 1; c.h = 2; return c; }
// note: no optional args in c

void p03_functions()
{
    printf("- 03 functions --------------\n");
    /*
      * in addition to primitive types, can return structs. CANNOT return arrays
      * additionally, the "void" keyword is used to indicate nothing returns
      * note: function overloading not allowed
    */
    int i = 4;
    printf("result1: %d\n", fn_example(3, &i));
    // can create a pointer to a function, ensure has same signature
    int (*myfn)(int, int*) = &fn_example;
    printf("result2: %d\n", myfn(4, &i));
    struct Cyl cc = tmp(); // returning a new struct
    printf("%d\n", cc.r * cc.h * 3);
}
void fn_define_later() { return 3; }


struct Rect1 {int x;int y;};
typedef struct Rect1 Rect1a; // can use typedef to simplify referencing
#define INIT_RECT1 {0,0}
typedef struct Circ1 { int r; }Circ1a; // can combine struct + typedef in one
void Circ1_init(Circ1a* c) { c->r = 0; } // alternate init method

typedef struct Rect2 {
    int x; int y;
    int (*area)(struct Rect2* r); // function pointer
}Rect2;
int rect2_area(Rect2* r) { return r->x * r->y; }
#define INIT_RECT2 {0,0,&rect2_area}
void p04_structs()
{
    printf("- 04 structs --------------\n");
    printf("Rect1 sz:%zu\n", sizeof(struct Rect1)); // function pointers take up space in a struct!
    struct Rect1 r1 = INIT_RECT1; // can initialize directly via each memory location
    Rect1a r1a = INIT_RECT1; // with typedef version, dont need struct
    Circ1a c1a;
    Circ1_init(&c1a); // 2-line method to initialize
    // combine multiple concepts: struct, typedef, function pointer, preprocessor command
    Rect2 r2 = INIT_RECT2; // declare & initialize in one line
    printf("area: %d\n", r2.area(&r2)); // example of using pointer function: no "self" in C
}

void p05_arrays() {
    // goal is to play around with arrays a little bit
    printf("- 05 arrays -------------------\n");
    int arr0[] = { 7,8,9 };
    printf("first value: %d\n", arr0[0]);
    printf("sz_top %zu\n", sizeof(arr0));
    printf("size: %zu\n", sizeof(arr0) / sizeof(arr0[0]));
    //print("size2:%d", len_arr(arr0));
}

void p06_libraries() { return; }// todo
void p07_memory_allocation() { return; }// todo
void p08_preprocessor() { return; }// todo
void p09_fileIO() { return; }// todo

int main() {
    p01_types();
    p02_operators();
    p03_functions();
    p04_structs();
    p05_arrays();
    p06_libraries();
    p07_memory_allocation();
    p08_preprocessor();
    p09_fileIO();

    return 0;
}