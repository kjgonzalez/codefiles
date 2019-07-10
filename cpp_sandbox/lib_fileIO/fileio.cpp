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

class FOUT{
    std::ofstream fout;
public:
    std::string filename;
    FOUT(std::string _filename){
        filename=_filename;
        fout.open(filename.c_str());
    }//initialization
}//FOUT



class FileOpen{
    std::ifstream fin;
    std::ofstream fout;
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
        if(mode=='w') fout << text.c_str();
        else {
            printf("WARNING: INCORRECT MODE.\n");
        }
    }//write

    std::string readline(){
        /* read out one line of text */
        std::string line;
        if(mode=='r'){
            getline(fin,line);
            line+="\n";
        }
        else {
            printf("ERROR: INCORRECT MODE.\n");
        }
        return line;
        // printf("%s",line.c_str());
    }//readline

    std::vector<std::string> readall(){
        fin.seekg(0,fin.beg); // go to start of filestream
        std::vector<std::string> raw;
        std::string line;
        while(!fin.eof()){
            getline(fin,line);
            line+="\n";
            raw.push_back(line);
            }
        return raw;
    }//readall

    void seek(int loc=0){
        fin.seekg(loc, fin.beg);
    }

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
    std::vector<std::string> alldata;
    alldata = f2.readall();
    for(int i=0;i<alldata.size();i++){
        printf("%s",alldata[i].c_str());
    }

    // at this point, read and write are working, but what if use wrong thing?
    FileOpen f3("test.txt",'w');
    f3.readline();


    FileOpen f4("test.txt",'r');
    f4.write("test");



    return 0;

}//main

















//eof
