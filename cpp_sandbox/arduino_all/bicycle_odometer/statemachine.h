#pragma once
/*
for the moment, define everything here in header, because don't want split things between interface and implementation
*/

enum STATE { STcomm, STreactive, STsleep, STsave }; // start state only exists during setup
typedef enum STATE st_t;

class StateMachine {
public:
    /* class with access to all other classes */
    st_t statecurr;
    st_t stateprev;
    StateMachine() {}
};//class-statemachine

class State {
public:
    st_t name;
    State(st_t nameval) { name = nameval; }
    void enter() {}
    void exit() {}
    void loop() {}

};//class-state

class Comm {

};//class-comm


