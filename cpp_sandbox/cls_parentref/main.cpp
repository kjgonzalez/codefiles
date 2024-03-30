/*
 * goal: make a class that has reference to class it was passed to, e.g. for state knowing the parent statemachine
 */

#include <iostream>

class Item1;
class Item2{public:
    int name=2;
    Item1 *parent;
};

class Item1{public:
    int name=1;
    Item2 *targ;
    void add(Item2 *it){
        targ = it;
        it->parent = this;
    }
};

int main(){
    printf("la\n");
    Item1 i1;
    Item2 i2;
    i1.add(&i2);
    //i2.parent=&i1;
    printf("i2: %d\n",i2.name);
    printf("parent: %d\n", i2.parent->name);


    


    return 0;


}

