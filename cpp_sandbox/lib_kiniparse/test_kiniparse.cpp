/*
simple demo of how ini parse works
*/

#include <iostream>
#include "kiniparse.hpp"


int main()
{
    printf("--- Kris' Ini Parse ---\n");
    std::string fpath = std::string(BASEPATH)+"/test1.ini";
    kip::IniParse ini(false);
    ini.load(fpath.c_str());

    printf("---\n");
    printf("parsed values: \n");
    std::cout << "mystr: " << ini.get<std::string>("mystr") << std::endl;
    std::cout << "myint: " << ini.get<int64_t>("myint") << std::endl;
    std::cout << "myfloat: " << ini.get<double>("myfloat") << std::endl;


    printf("exiting...\n");
    return 0;


}



