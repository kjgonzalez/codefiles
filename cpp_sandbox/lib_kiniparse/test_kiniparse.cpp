/*
simple demo of how ini parse works
*/

#include <iostream>
#include "kiniparse.hpp"


int main()
{
    printf("--- Kris' Ini Parse ---\n");
    std::string fpath = std::string(BASEPATH)+"/test.ini";
    IniParse ini(false);
    ini.load(fpath.c_str());

    printf("---\n");
    printf("parsed values: \n");
    std::cout << "mystr: " << ini.get<std::string>("mystr") << std::endl;
    std::cout << "myint: " << ini.get<int64_t>("myint") << std::endl;
    std::cout << "myfloat: " << ini.get<double>("myfloat") << std::endl;
    std::cout << "listint: " << ini.get <std::vector<int64_t>>("list_int").size() << std::endl;
    std::cout << "listdbl: " << ini.get <std::vector<double>>("list_dbl").size() << std::endl;
    std::cout << "liststr: " << ini.get <std::vector<std::string>>("list_str").size() << std::endl;

    printf("exiting...\n");
    return 0;


}



