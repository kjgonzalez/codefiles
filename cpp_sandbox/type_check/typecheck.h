/*
this header file is for having overloaded function "gettype", to assist with
knowing variable type when debugging
*/
#include <iostream>
#include <vector>
#include <string.h>

std::string gettype(std::string sample){
    return         "std::string";
}

std::string gettype(int sample){
    return         "int";
}

std::string gettype(float sample){
    return         "float";
}

std::string gettype(double sample){
    return         "double";
}

std::string gettype(char sample){
    return         "char";
}

std::string gettype(bool sample){
    return         "bool";
}
