/*
composition-only example
src: http://www.cplusplus.com/forum/beginner/108574/
will have 2 classes, people & birthday. every person has a birthday, so inside
    people class will store birthday object
*/

#include <iostream>
#include <string>
using namespace std;

// this class, Birthday, will become a part of the People class. People aren't
//  a subset of Birthday, nor vice versa. example of a "has a" (composition) structure
class Birthday{
    int month, day, year;
public:
    Birthday(int cyear, int cmonth, int cday){month = cmonth; day = cday; year = cyear;}
    void printDate(){printf("%i-%i-%i\n",year,month,day);}
    void changeDate(int cyear, int cmonth, int cday){month = cmonth; day = cday; year = cyear;}
}; //Birthday

class People{
    string name; Birthday bday;
    int height; //cm
public:
    People(string cname, Birthday cdateOfBirth, int cheight=171):
        name(cname),bday(cdateOfBirth),height(cheight)
        {} // not sure why, but this is requireed
        // ":" required, part of declaring other object (not sure why)

    void printInfo(){
        printf("name: %s\n",name.c_str());
        printf("bday: ");bday.printDate();
        printf("height: %i\n",height);
    }//printInfo
    void changeBday(int cyear, int cmonth, int cday){
        bday.changeDate(cyear,cmonth,cday);
    }//changeBday
};//People

int main() {
    // //original
    // Birthday birthObject(1997,7,9);
    // People persObj("Lenny the Cowboy", birthObject);

    // another way: pass by value directly in instatiation
    People persObj("Lenny the Cowboy", Birthday(1997,7,9) , 170);

    persObj.changeBday(1990,9,6);
    persObj.printInfo();

}
