/*
date: 190709
objective: simplify the mountain of shit that is cpp file i/o into a class that
    lets you do things much more easily.


basic example:
f=open(filename,'w')
f.write(someStringThatHasNewLine)
f.write(anotherString)
f.close()

f=open(filename) //for reading
f.asVector()
f.readline()
f.len


minor improvements:
STATUS | DESCRIPTION
wait   | be able to use printf formatting directly in function


*/


#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <fstream>
#include "io_help.h"

int main(){
    FileOpen f("test.txt",'w');
    for(int i=0;i<3;i++){
        char buffer[50];
        sprintf(buffer,"hello world %d\n",i);
        printf("hello world %d\n",i);
        f.write(buffer);
    }//forloop
    f.close();
    FileOpen f2("test.txt",'r');
    printf("%s",f2.readline().c_str());
    std::vector<std::string> alldata;
    alldata = f2.readall();
    for(int i=0;i<alldata.size();i++){
        printf("%s",alldata[i].c_str());
    }

    // at this point, read and write are working, but what if use wrong thing?
    FileOpen f3("test.txt",'w');
    printf("first line: %s",f3.readline().c_str());

    FileOpen f4("test.txt",'r');
    f4.write("test");


    // one last example
    FileOpen f5("test.txt",'w');
    f5.write("hello world\n");
    f5.write("some more stuff to save\n");
    


    return 0;
}//main
