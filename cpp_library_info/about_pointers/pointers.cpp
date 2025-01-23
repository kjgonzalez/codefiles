/*
how to generally work with pointers

* pointer basics
* using pointers with containers (vectors)
* edge cases
* smart pointers
* unique pointers
*/


#include <vector>
#include <memory>
typedef std::vector<uint8_t> bvec_t; // vector of bytes

class Rect
{
public:
    int x, y;
    Rect(int x = 0, int y = 0) :x(x), y(y) {};
    int area() { return x * y; }
};

void fn1_basics()
{
    int someval = 1;
    int* pval = &someval;
    printf("-- fn1_basics --\n");
    printf("%d (%p), %d (%p)\n", someval, &someval, *pval, pval);

}

void _pass_in(int byval, int& byref, int* byptr)
{
    printf("val: %d (%p). ", byval, &byval);
    printf("ref: %d (%p). ", byref, &byref);
    printf("ptr: %d (%p)\n", *byptr, byptr);
}

void fn2_pass_in()
{
    printf("-- fn2_pass_in --\n");
    int val0 = 23;
    _pass_in(val0, val0, &val0);

    int* val1 = new int(3); // dynamic memory alloc req's that user also delete when done
    _pass_in(*val1, *val1, val1);
    delete val1;
}

void _pass_class(Rect* rr){ printf("area: %d\n", rr->area()); }

void fn3_class()
{
    printf("-- fn3_class --\n");
    Rect r(3, 4);
    _pass_class(&r);

}

void _pass_vector(bvec_t vval, bvec_t &vref, bvec_t *vptr)
{
    printf("val: %d, %llu, %p. ", vval[1],vval.size(),&vval);
    printf("ref: %d, %llu, %p. ", vref[1],vref.size(),&vref);
    printf("ptr: %d, %llu, %p. ", (*vptr)[1],vptr->size(),vptr);
}

void fn4_using_vectors()
{
    bvec_t bv = { 2,4,6,8,16 };
    _pass_vector(bv, bv, &bv);

}

Rect* badptr_dangling(int x, int y)
{
    /* this function incorrectly returns the address to a local entity that gets freed when the 
      function exits. this means the address unexpectedly points to empty memory, a dangling 
      pointer. NOTE: normally this function would create dangling pointer, but seems to be handled 
      by visual studio
    */
    Rect r(x, y);
    printf("dangler area: %d\n", r.area()); 
    return &r;
}

Rect* badptr_memleak(int x, int y)
{
    /* 
    This function creates a burden of dynamic allocation responsibility on the user of the 
      function. If the data at the address isn't deleted, then you have a memory leak. One 
      way to avoid this risk is using a shared pointer, see next function.
    
    */
    return new Rect(x, y);
}

void fn5_bad_pointers()
{
    /* demonstrate (incl. with VS diagnostic tool) how can have pointer issues */

    printf("dangling pointer\n");
    Rect* pr0 = badptr_dangling(3,4);
    printf("dangler_pt2: %d (%p)\n\n", pr0->area(), pr0);
    
    printf("memory leak\n"); //note: visual studio makes easier to visualize, with snapshots
    Rect* pr1;
    unsigned int usage = 0;
    for (int i = 0; i < 10; i++) {
        pr1 = badptr_memleak(i, i + 1); // every loop, usage goes up. memory not being cleared 
        usage += sizeof(*pr1);
        printf("used: %u. ", usage);
        // solution: clear memory with "delete" (or delete[] for array)
        // delete pr1;
        //note: this memory will only be cleared when entire program exits.
    }
    printf("\n");
}

std::unique_ptr<Rect> unique_ptr(int x, int y)
{
    /* convenient way to deal with dynamic memory alloc, let compiler know when to free memory */
    std::unique_ptr<Rect> pr(new Rect(x, y));
    return pr;
}

void fn6_uniqueptr()
{
    /* unlike strictly using new/delete, unique_ptr keeps track of deallocation */

    std::unique_ptr<Rect> pr;
    for (int i = 0; i < 10; i++)
    {
        pr = unique_ptr(i, i + 1); // memory is allocated once, then doesn't increase
    }
}



int main()
{
    printf("hi\n");
    // basics
    fn1_basics();
    fn2_pass_in();
    fn3_class();
    fn4_using_vectors();
    fn5_bad_pointers();
    fn6_uniqueptr();
/* 
k250123: FIX THIS vvvvvvvvvvvvvv
 *
basic info on how to use pointers effectively.

* size of a pointer (size of addressable data, e.g. 64bit)
* pointer object, passing between functions
* returning pointer to object... ?

notes:
* passing by reference & pointer seem equivalent when passing in for memory usage
* returning a pointer is better than returning a value for memory usage
* memory space can sometimes be reused intelligently by the compiler
*/

#include <iostream>
using std::cout;
using std::endl;

class Rect{
public:
    int x,y;
    Rect(int x_=0, int y_=0){x=x_;y=y_;}
    int area(){return x*y;}
};

void printinfo(Rect* rptr){ cout << rptr << " " << rptr->x << " " << rptr->y << endl;}

void passing_in(Rect r_val, Rect &r_ref,Rect *r_ptr){
    // the three methods of passing in a variable, and how it's tracked in memory
    printf("- passing_in function --------------------\n");
    cout << "rval addr: "; printinfo(&r_val);
    cout << "rref addr: "; printinfo(&r_ref);
    cout << "rptr addr: "; printinfo(r_ptr);
}

Rect return_val(){ 
    Rect r(1,1); 
    cout << "func-val:  "; printinfo(&r);
    return r;
}

Rect* return_ptr(){ 
    Rect* rptr = new Rect(2,2); 
    cout << "func-ptr:  "; printinfo(rptr);
    return rptr; 
}

int main(){
    printf("about: pointers and their usage\n");
    // basics: accessing pointer information
    int16_t var=3;
    int16_t* ptr=&var;
    cout << "var: " << var << ". size_bytes: ("<< sizeof(var) << ")\n";
    cout << "var_addr: "<< &var <<"\n";
    cout << "ptr: " << ptr << ". size_bytes: ("<< sizeof(ptr) << ")\n";
    cout << "ptr_val: "<< *ptr << "\n";

    Rect r1(2,3);
    Rect* pr = &r1; // use reference to one entity for pointer variable
    Rect* r2 = new Rect(4,5); // instantiate entity in same line as declare pointer

    printf("obj: %d. %d \n",r1.x,r1.area());
    printf("obj-ptr1: %d. %d \n",pr->x,pr->area());
    printf("obj-ptr2: %d. %d \n",r2->x,r2->area());
    
    // how to pass entities in differently
    cout << "r1 addr:   "; printinfo(&r1);
    cout << "r2 addr:   "; printinfo(r2);// << r2 << endl;
    passing_in(r1,r1,&r1);

    // how to return entities differently
    printf("- return from func ------------\n");
    Rect retval = return_val();
    cout << "main-val:  "; printinfo(&retval);
    
    Rect* retptr = return_ptr();
    cout << "main-ptr:  "; printinfo(retptr);

    return 0;
}

// eof 

