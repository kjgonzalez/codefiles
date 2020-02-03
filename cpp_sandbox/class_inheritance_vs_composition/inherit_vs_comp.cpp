/*
date: 200203
objective: class inheritance vs composition

basic thing to remember:
* "inheritance" = "X is a Y" (human is a person)
* "composition" = "Y has an X" (a person has a name / height / weight)

for example:
animals poop
dogs bark
cats meow
robots have batteries
robo dog can bark but doesn't poop
thus, inefficient to have:
    animals
        dogs
        cats
    robots
        dogs

instead: will use composition:
name
bark
meow
poop
powerType

and thus:
dog: name-poop-bark
cat: name-pooper-meow
robodog: name-powerType-bark
*/

#include <iostream>
#include <string>
using namespace std;

// INHERITANCE-BASED SETUP
struct Animal {
    string name;
    void poop(){printf("%s poops.\n",name.c_str() );}
};

// Derived struct
struct Dog: public Animal {
    // if this weren't a struct, you'd need a "public" here
    void bark(){printf("%s barks.\n",name.c_str() );}
};

struct Cat: public Animal {
    void meow(){printf("%s meows.\n",name.c_str() );}
};

// COMPOSITION BASED SETUP
struct Bark{
    void bark(){printf("It barks.\n");}
};



void printsep(){printf("------------------\n");}
int main(void) {

    printf("INHERITANCE EXAMPLES ====================================\n");
    Animal bear;
    bear.name="bob";
    bear.poop();

    printsep();
    Dog dog;
    dog.name="spot";
    dog.poop();
    dog.bark();

    printsep();
    Cat cat;
    cat.name = "whiskers";
    cat.poop();
    cat.meow();
    // cat.bark(); // would result in an error

    printf("COMPOSITION EXAMPLES ====================================\n");


   return 0;
}
