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
#include <map>
#define nl "\n"

enum ST {OFF,RDY,WSH,SPN,STOP};

struct State{
    enum ST name;
    void *parent;
    virtual void enter(){}
    virtual void exit(){}
    virtual enum ST loop(){
        printf("wrong" nl);
        return ST::STOP;}
};

struct StateMachine{
    std::map<enum ST,State *> d;
    enum ST curr;
    enum ST prev;
    enum ST res;
    bool exit=false;
    bool started=false;
    StateMachine(){}
    void add(enum ST enumstate,State *state){
        if(d.size()==0){
            curr=enumstate;
            prev=enumstate;
        }
        d[enumstate]=state;
        state->parent = this;
    }
    void printsaved(){
        printf("saved states:" nl);
        for(auto id:d){
            printf("%d" nl,(int) id.first);
        }
    }
    void loop(){
        if(!started){ d[curr]->enter();started=true; }
        printf("loop" nl);

        res = d[curr]->loop();
        if(res==ST::STOP){d[curr]->exit();exit=true;return;}
        else if(res!=curr){
            d[curr]->exit();
            d[res]->enter();
            prev=curr;
            curr=res;
        }
    }//loop
};

struct StReady:State{
    enum ST name = RDY;
    int count=0;
    void enter(){printf("rdy: enter" nl);}
    void exit(){printf("rdy: exit" nl);}
    enum ST loop(){
        count++;
        if(count<5) return name;
        else return ST::STOP;
    }
};

int main(){
    printf("hi" nl);
    StateMachine sm;
    sm.add(RDY,new StReady);
    sm.printsaved();
    while(!sm.exit){
        sm.loop();
    }
    return 0;
}

