/*
state machine basics
*/

#include <string>
#include <iostream>

class StateTemplate {
public:
    std::string name;
    virtual void enter() { printf("Entering %s\n", name.c_str()); };
    virtual void exit() { printf("Exiting %s\n", name.c_str()); };
    virtual StateTemplate* run() = 0;
};

class StateStop :public StateTemplate { // example of one class
public:
    StateStop() {
        name = "stop";
    }
    StateTemplate* run() {
        printf("running %s\n", name.c_str());
        return this;
    }
};

class StateMachine {
public:
    StateTemplate* active;
    StateTemplate* tmp;
    void start(StateTemplate* state0) {
        active = state0;
        active->enter();
    }
    void mainloop() {
        tmp = active->run();
        // sleep(1); // for a demo, should have easy way to slow down computation to see all steps
        if (tmp != active) {
            active->exit();
            active = tmp;
            active->enter();
        }
    }

};

int main(){
    StateStop st_stop;
    StateMachine sm;
    sm.start(&st_stop);
    while(true){
        sm.mainloop();  // this allows things to happen outside of state machine loop 
    }                   // as well, but "while" can be in mainloop
    return 0;
}
