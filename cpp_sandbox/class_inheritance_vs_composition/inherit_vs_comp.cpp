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
name - bark - meow - poop - powerType
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
    string name; // to save on memory, probably would keep this info only in child class
    void poop(){printf("%s poops.\n",name.c_str() );}
};

// Derived struct
class Dog: public Animal {
public:
    void bark(){printf("%s barks.\n",name.c_str() );}
};

class Cat: public Animal {
public:
    void meow(){printf("%s meows.\n",name.c_str() );}
};

// COMPOSITION BASED SETUP
class Bark{
    string name,loudness; // to save on memory, probably would keep this info only in child class
public:
    Bark(string name_,string loudness_){name=name_,loudness=loudness_;}
    void bark(){printf("%s barks %s.\n",name.c_str(),loudness.c_str());}
};
class Meow{
    string name;
public:
    Meow(string name_){name=name_;}
    void meow(){printf("%s meows.\n",name.c_str());}
};
class Poop{
    string name;
public:
    Poop(string name_){name=name_;}
    void poop(){printf("%s poops.\n",name.c_str());}
};
class Dog2{
    string name; Poop p; Bark b;
public:
    Dog2(string name_,string loudness_):
        name(name_),p(Poop(name_)),b(Bark(name_,loudness_)){}
        // composition items can be instantiated anywhere, including in macro class initialization
    void bark(){b.bark();}
    void poop(){p.poop();}
};
class Cat2{
    string name; Poop p; Meow m;
public:
    Cat2(string name_):
        name(name_),p(Poop(name_)),m(Meow(name_)){}
    void poop(){p.poop();}
    void meow(){m.meow();}
};

class Batt{
    string name,type;
public:
    Batt(string name_,string type_){name=name_;type=type_;}
    void TypeReq(){printf("%s needs battery type %s",name.c_str(),type.c_str());}
};

class RoboDog{
    string name; Bark b; Batt ba;
public:
    RoboDog(string name_,string loudness_,string batt_type_):
        name(name_),b(Bark(name_,loudness_)),ba(Batt(name_,batt_type_)){}
    void bark(){b.bark();}
    void reqBatt(){ba.TypeReq();}
};

void printsep(){printf("------------------\n");}
int main(void) {
    // compress inheritance into collapsible if-statement
    if(true){
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
    }

    printf("COMPOSITION EXAMPLES ====================================\n");
    Dog2 dog2("spike","loudly");
    dog2.bark();
    dog2.poop();

    printsep();
    Cat2 cat2("kitty");
    cat2.meow();
    cat2.poop();

    printsep();
    RoboDog pup("Sparky","mildly","AA");
    pup.bark();
    pup.reqBatt();

   return 0;
}
