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
#include <iostream> // todo: delme
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
    return &r; // note: correctly raises warning about bad return address
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
    printf("-- fn6_uniqueptr --\n");
    std::unique_ptr<Rect> pr;
    for (int i = 0; i < 10; i++)
    {
        pr = unique_ptr(i, i + 1); // memory is allocated once, then doesn't increase
    }
}

void shared_recurse(std::shared_ptr<Rect> rec,int depth=2)
{
    printf("current use count: %d\n", rec.use_count());
    if (depth > 0) shared_recurse(rec, depth - 1);
    printf("current use after: %d\n", rec.use_count());
}

void fn7_sharedptr()
{
    printf("-- fn1_sharedptr --\n");
    // normally, object is declared / used like so:
    // Rect r(3, 4); r.area();
    std::shared_ptr<Rect> rr = std::make_shared<Rect>(3, 4); // how to initialize with shared
    printf("sharedptr area: %d\n", rr->area()); // access declared object
    printf("mem loc: %p\n", rr.get());
    printf("current use count: %d\n", rr.use_count());
    shared_recurse(rr);
    printf("current use after: %d\n", rr.use_count());
    // can also swap memory addresses with another item... seems quite helpful
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
    fn7_sharedptr();
    return 0;
}
// eof
