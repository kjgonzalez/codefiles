/*
objective: learn how to understand and use the arrow operator (->) to refer to
  an object with a pointer instead of passing the object directly (using more
  memory space)

src: https://www.tutorialspoint.com/cplusplus/cpp_member_operators.htm
src: http://www.cplusplus.com/doc/tutorial/classes/
src: http://www.cplusplus.com/doc/tutorial/pointers/

as said in one of the sources:
Simply saying: To access members of a structure, use the dot operator. To
  access members of a structure through a pointer, use the arrow operator.

*/

#include <iostream>
#include <math.h>

//first, need to make a simple class that will be used
class rect{
  public:
    int width, height;
    rect(int wd, int ht){
      width = wd;
      height = ht;
    }//constructor
    // in this example, will make everything public.
    int area(void)  {return(width*height);}
    int perim(void) {return(2*(width+height));}
};

// next, need a function that takes in an address as an argument (received as \
  a pointer). remember, pointers hold addresses.
int boxareas(rect *a, rect *b){ // receive pointers of type rect
  int sum = 0;
  sum += a->area(); // here, calling "area member of object at address of ptr a"
  sum += b->area();
  return sum;
}//boxareas

//finally, initialize an object and pass the address to the function
int main(){
  rect r(3,4); //here, you have a direct object
  rect r2(5,6);

  // just for a bit of practice, want to make a pointer to object 'r'
  int a=0;
  int *p; // pointer int
  p=&a; // value the pointer holds is the address of 'a'
  // alternatively: assign address of a to p
  *p = 3; // assign '3' to value slot at p
  std::cout << "value:" << p << '\n';

  // so next, want to make a rect pointer:
  // rect *rp =  &r; // assign address of r to pointer rp
  // rect *rp2 = &r2; // etc

  // kjgnote: most explicit method: create pointer, store address, pass ptr to function
  // std::cout << "combined areas: "<<boxareas(rp,rp2) << "\n";

  // slimmed down method: pass address of object to a function that uses pointers
  std::cout << "combined areas: "<<boxareas(&r,&r2) << "\n";

  /*
  kjgnote: short summary of what's going on above:
    first, create some number of objects with members, which can either be
      variables or functions
    next, have a function that doesn't receive a value directly, but instead
      the address of a value that is immediately assigned to a pointer argument
    finally, in the function, refer to the original object by using the
      arrow operator to access the object at the address of the pointer.

    e.g.: in the above function:
    "assign to the value of sum the member 'area' of the object that is at
      the address of pointer 'a'"

  */


  // note, this is using the dot operator. here, we directly access the object
  std::cout << "stuff1: "<<r.area() << " "<< r.perim() << "\n";
  std::cout << "stuff2: "<<r2.area() << " "<< r2.perim() << "\n";

  //now, want to access the members of each object through a pointer, not directly




  return 0;
}//main
