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


/* at this point, want to be able to work on a file, which would have multiple
    lines. load the file, swap it, and save it to a new file */

int main(int argc,char **argv){
    printf("= kjg cipher ========== \n");
    // std::string input = argv[1];
    if(0){
        std::string input;
        input="test\nitem";
        printf("input : %s\n",input.c_str());
        printf("output: %s\n",swapLine(input).c_str());
    }

    std::vector<std::string> raw=readFile("sample.txt");
    printf("original text:\n");
    disp(raw);

    printf("swapped text:\n");
    disp(swapParagraph(raw))
    // std::vector<std::string> raw2=swapParagraph(raw);
    // raw=swapParagraph(raw);
    // disp(raw);
    // for(int i=0;i<raw.size();i++){
    //     std::cout << swapLine(raw[i]) << '\n';
    // }
    // std::cout << readFile("sample.txt");
    // now, work on reading from a file (first)


}//int main
