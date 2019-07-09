/*
date: 190709
objective: simplify the mountain of shit that is cpp file i/o into a class that lets you do things much more easily.

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


class FileOpen{
    std::ifstream fin;
    std::ofstream fout;
    int mode;
public:
    std::string filename;
    char mode;
    FileOpen(std::string _filename,char _mode='r'){
        filename=_filename;
        mode = _mode;
        if(mode=='w'){
            fout.open(filename.c_str());
        }//if-'w'

        else if(mode=='r'){
            // printf("read mode\n");
            fin.open(filename.c_str());
        }//if-'r'
        else printf("mode not recognized\n");
    }//initialize
    void write(std::string text){
        /* write out a line of text to file */
        fout << text.c_str();
    }//write

    std::string readline(){
        /* read out one line of text */
        std::string line;
        getline(fin,line);
        line+="\n";
        return line;
        // printf("%s",line.c_str());
    }//readline
    std::vector<std::string> readall(){
        std::vector<std::string> raw;
        fin.seekg
    }//readall
    void close(){
        /* close the current stream */
        if(mode=='w') fout.close();
        else if(mode=='r') fin.close();
    }//close

}; //class FileOpen

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
    printf("%s",f2.readline().c_str());

    return 0;

}//main

















//eof
