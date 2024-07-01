/*
create basic states here that the program will follow
*/

//#include <string>

class StateTemplate {
public:
    string name;
    virtual void enter() { printf("Entering %s\n", name.c_str()); };
    virtual void exit() { printf( "Exiting  %s\n", name.c_str()); };
    virtual StateTemplate* run() = 0;
};

class StateActive : public StateTemplate {
public:
    StateActive() {
        name = "active";
    }
    StateTemplate* run() {
        printf("running %s\n", name.c_str());
        return this;
    }
};

class StatePassive :public StateTemplate {
public:
    StatePassive() {
        name = "passive";
    }
    StateTemplate* run() {
        //printf("running %s\n", name.c_str());
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
        if (tmp != active) {
            active->exit();
            active = tmp;
            active->enter();
        }
    }

};