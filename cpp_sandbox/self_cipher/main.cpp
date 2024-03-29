/*
DateCreated: 190612
Objective: create simple cipher program, with some simple features:
1. given a string / file, scramble the letters
2. have a symmetric cipher that can unscramble everything as well
3. given the correct password, continue with actually processing the file

KJG190612: in the future, may need better argparser:
https://github.com/jarro2783/cxxopts
https://www.reddit.com/r/cpp/comments/4zhm2n/which_library_would_you_recommend_for_parsing/

KJG190612: ok, it may be possible to initially just use an ascii table cipher, where you rotate one value for another.



compile: g++ argsin.cpp -o test
*/
// one two three


#include <iostream>
#include <fstream> // I/O operations
#include <stdio.h>  // needed for splitting a string & sometimes I/O operations
#include <vector>
#include <string.h>
char swapLetter(char letter){
    /* Return an offset letter from given. simplest cipher possible. */
    if(letter<32 || letter>125){
        // ensure no issues with characters not in range
        return letter;
    }//if in range
    int newval = letter+47;
    if(newval>125) newval-=94;
    return char(newval);
}//swapLetter

std::string swapLine(std::string line){
    /* Return entirely swapped line of text. ignores characters not part of
        swap. */
    std::string line2;
    for(int i=0;i<line.length();i++){
        line2.push_back(swapLetter(line[i]));
    }
    return line2;
}//swapLine

std::vector<std::string> swapParagraph(std::vector<std::string> raw){
    /* Replace all given lines with ciphered text */
    std::vector<std::string> raw2;
    for(int i=0;i<raw.size();i++){
        raw2.push_back(swapLine(raw[i]));
    }//forloop
    return raw2;
}//swapParagraph

void disp(std::vector<std::string> text){
    /* simple way to display vector string */
    for(int i=0;i<text.size();i++) std::cout << text[i] << '\n';
}//disp

std::vector<std::string> readFile(std::string filename){
    /* read in file, and return as a string vector */
    std::ifstream fin(filename.c_str());
    std::vector<std::string> raw;
    std::string line;
    while(!fin.eof()){
        getline(fin,line); // perhaps a native C/C++ function?
        raw.push_back(line);
    }
    fin.close();
    return raw;
}//readFile

void writeFile(std::string filename,std::vector<std::string> text){
    /* Given a filename and a vector of strings, save text to a file all at
        once. */
    FILE *f_out = fopen(filename.c_str(),"w");
    for(int i=0;i<text.size();i++){
        fprintf(f_out,text[i].c_str());
        if(i<text.size()-1) fprintf(f_out,"\n"); // prevents extra newlines
    }//forloop
}//writeFile

/* finally, want to prevent auto decoding without having a password, so store
    something in memory and ensure that it matches.
    */

int checkPassword(std::string attempt){
    int result = strcmp("dimeloprincesa",attempt.c_str());
    return result;
}

/* at this point, want to be able to work on a file, which would have multiple
    lines. load the file, swap it, and save it to a new file */

int main(int argc,char **argv){
    if(strcmp(argv[1],"--help")==0){
        printf("usage: swapper <password> <filepath>\n");
        printf("note: given file will be overwritten\n");
        return 0;
    }
    printf("= kjg swapper ========== \n");
    if(checkPassword(argv[1]) !=0){
        std::cout << "incorrect password.\n";
        return 0;
    }

    printf("Opening file %s ...\n",argv[2]);
    std::vector<std::string> raw=readFile(argv[2]);

    printf("Swapping text... \n");
    std::vector<std::string> raw2=swapParagraph(raw);
    printf("overwriting original file...\n");
    writeFile(argv[2],raw2);
    printf("complete.\n");
}
