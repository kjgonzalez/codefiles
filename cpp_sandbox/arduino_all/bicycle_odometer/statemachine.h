#pragma once
/*
for the moment, define everything here in header, because don't want split things between interface and implementation
*/

enum STATE { STcomm, STreactive, STsleep, STsave }; // start state only exists during setup
typedef enum STATE st_t;

class StateMachine {
public: /* class with access to all other classes */
    st_t statecurr;
    st_t stateprev;
    StateMachine() {}
    void loop(){

    }//loop
};//class-statemachine

class State {
public:
    st_t name;
    State(st_t nameval) { name = nameval; }
    void enter() {}
    void exit() {}
    st_t loop() {return name}
};//class-state

class Comm:State{
    void enter(){
        printf("enter comm\n");
    }//void enter
    void exit(){
        print("exit comm\n");
    }//exit
    st_t loop(){
        print("loop comm\n");
        return name;
    }//loop
};//class-comm


