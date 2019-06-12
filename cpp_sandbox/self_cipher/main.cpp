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

char swapLetter(char letter){
    /* Return an offset letter from given. simplest cipher possible. */
    if(letter<33 || letter>126){
        // ensure no issues with characters not in range
        return letter;
    }

    int newval = letter+27;
    if(newval>126) newval-=94;
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

int main(int argc,char **argv){
    printf("= kjg cipher ========== \n");
    std::string input = argv[1];

    input="test\nitem";
    printf("input : %s\n",input.c_str());
    printf("output: %s\n",swapLine(input).c_str());

}//int main
