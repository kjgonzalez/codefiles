/*
mini example of kargparse

kargparse: kjg-basic arg parsing library, intended to be in-house solution so another waiver isn't needed...

*/

#include <assert.h>
#include <iostream>
#include "kargparse.hpp"
#include <string>
#include <map>

using std::cout;
using std::endl;
using std::string;

int main(int argc, char** argv)
{
    /*
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
    KArgParser ap;
    ap.add_desc("my program, does things");
    ap.add_req("mybool", "boolean", atype_bool);
    ap.add_req("myint", "integer", atype_int);
    ap.add_req("myuint", "unsigned int", atype_uint);
    ap.add_req("mydouble", "double precision", atype_double);
    ap.add_req("mystr", "string value (use quotes)", atype_str);
    ap.parse(argc,argv);

    bool mybool;
    long myint;
    unsigned long myuint;
    double mydouble;
    std::string mystr;



    ap.get("mybool", mybool);
    ap.get("myint", myint);
    ap.get("myuint", myuint);
    ap.get("mydouble", mydouble);
    ap.get("mystr", mystr);

    cout << "mybool: " << mybool << endl;
    cout << "myint: " << myint << endl;
    cout << "myuint: " << myuint << endl;
    cout << "mydouble: " << mydouble << endl;
    cout << "mystr: " << mystr << endl;
    printf("done\n");
    
    return 0;
}



// eof

