/* goal is to make very basic example of a statemachine in c++ code, to get 
 *  familiar with general structure / conventions.

a washing machine must be implemented as a state machine with the following states:
* off
* ready
* washing
* spindry
transitions:
* off leads to ready
* ready leads to either off or washing
* washing >> spindry
* spindry >> ready


*/

#include <iostream>
#define nl "\n"



int main(){
    printf("hi" nl);
    std::cout << "test" nl;
    return 0;
}

