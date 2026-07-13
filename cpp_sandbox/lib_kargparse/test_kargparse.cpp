/*
mini example of kargparse

kargparse: kjg-basic arg parsing library, intended to be in-house solution so another waiver isn't needed...

KArgParser argp();
argp.add_description("program description")
argp.add_req("name1","description",type)
argp.add_opt("name2","description",type,defaultval)
argp.add_flg("name3","description",defaultval)
argp.parse(argc,argv)
argp.get("name",&var)
private:
argp._help()


*/

#include <assert.h>
#include <iostream>
#include "kargparse.hpp"
#include <string>
#include <map>

using std::cout;
using std::endl;
using std::string;

int main()
{
    //bool minicheck = true;
    //cout << "orig: " << minicheck << endl;
    //minicheck = !minicheck;
    //cout << "toggle1: " << minicheck << endl;
    //minicheck = !minicheck;
    //cout << "toggle2: " << minicheck << endl;
    //exit(0);
    printf("- layout 1: all required -----------------\n");
    char* argv1[] = {
        (char*)"/path/to/main.program",
        (char*)"0",
        (char*)"-12",
        (char*)"34",
        (char*)"5.6",
        (char*)"seven eight"
    };
    int argc1 = 6;
    // ---
    KArgParser ap(true);
    ap.add_desc("layout 1: all required");
    ap.add_req("mybool", "boolean", atype_bool);
    ap.add_req("myint", "integer", atype_int);
    ap.add_req("myuint", "unsigned int", atype_uint);
    ap.add_req("mydouble", "double precision", atype_double);
    ap.add_req("mystr", "string value (use quotes)", atype_str);
    ap.parse(argc1,(char**) argv1);
    // ---
    cout << "mybool: " << ap.get<bool>("mybool") << endl;
    cout << "myint: " << ap.get<int64_t>("myint") << endl;
    cout << "myuint: " << ap.get<uint64_t>("myuint") << endl;
    cout << "mydouble: " << ap.get<double>("mydouble") << endl;
    cout << "mystr: " << ap.get<string>("mystr") << endl;
    ap.reset();

    printf("- layout 2: mixed -----------------\n");
    char* argv2[] = {
        (char*)"/path/to/main.program",
        (char*)"-12",
        (char*)"3.4",
        (char*)"--name",
        (char*)"john",
        (char*)"--save",
    };
    int argc2 = 6;
    // ---
    ap.add_desc("layout 2: mixed");
    ap.add_req("myint", "integer", atype_int);
    ap.add_req("mydouble", "double precision", atype_double);
    ap.add_opt<string>("name", "person's name", "default");
    ap.add_opt<bool>("save", "save file", false);
    ap.parse(argc2, (char**)argv2);
    // ---
    cout << "myint: " << ap.get<int64_t>("myint") << endl;
    cout << "mydouble: " << ap.get<double>("mydouble") << endl;
    cout << "name: " << ap.get<string>("name") << endl;
    cout << "save: " << ap.get<bool>("save") << endl;
    ap.reset();
    printf("- layout 3: swapped positions -----------------\n");
    char* argv3[] = {
        (char*)"/path/to/main.program",
        (char*)"-12",
        (char*)"3.4",
        (char*)"--save",
        (char*)"--name",
        (char*)"james",
    };
    int argc3 = 6;
    ap.add_desc("layout 2: mixed");
    ap.add_req("myint", "integer", atype_int);
    ap.add_req("mydouble", "double precision", atype_double);
    ap.add_opt<string>("name", "person's name", "default");
    ap.add_opt<bool>("save", "save file", false);
    ap.add_flag("nocuda", "disable cuda", true);
    ap.parse(argc3, (char**)argv3);
    cout << "myint: " << ap.get<int64_t>("myint") << endl;
    cout << "mydouble: " << ap.get<double>("mydouble") << endl;
    cout << "name: " << ap.get<string>("name") << endl;
    cout << "save: " << ap.get<bool>("save") << endl;
    cout << "cuda: " << ap.get<bool>("nocuda") << endl;

    printf("done\n");
    
    return 0;
}



// eof

