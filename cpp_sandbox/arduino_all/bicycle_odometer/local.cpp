/*
local attempt to do things
*/

#include <iostream>
#include <chrono>
#include "odometer/StateMachine.hpp"
//using namespace std;
//using namespace std::chrono;


//uint64_t now_ms() {
//    // return epoch time in microseconds
//    return std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch()).count();
//}
//
//void sleep(int s) {
//    // basic sleep a given number of seconds, using ctime
//    uint64_t tfinal = now_ms()+s*1000;
//    while (now_ms() < tfinal);
//}

int return1(int a) { return 1*a; }

int call_2(int callable(int val) ) {
    return callable(3) + 1;
}

int main() {
    printf("Starting\n");

    printf("test: %d\n", call_2(return1));
    return 0;

    StateStop ststop;
    StateMachine sm;

    sm.start(&ststop);
    
    //while (true) { sm.mainloop(); }


    return 0;
}

// eof
