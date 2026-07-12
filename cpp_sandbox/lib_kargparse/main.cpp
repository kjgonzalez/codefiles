/*
mini example of kargparse

kargparse: kjg-basic arg parsing library, intended to be in-house solution so another waiver isn't needed...

*/

#include <assert.h>
#include <iostream>
#include "kargparse.hpp"
#include <string>
#include <map>
//#include <vector> // todo

// todo: make an enum for allowed types (bool, int, uint, double, string)



using std::string;

enum Argtype_ 
{
    atype_bool,
    atype_int, 
    atype_uint, 
    atype_double, 
    atype_str };
typedef enum Argtype_ Argtype; // so don't need to write "enum"
// todo: macro to convert varname to string

class KArgParser
{
    struct Argitem
    {
        string  name;
        string  desc;
        Argtype atype;
        bool    valb;
        long    vali;
        unsigned long  valu;
        double vald;
        char valc[100];

        void setval(char* val)
        {
            switch(atype){
                case atype_uint:{
                    printf("  parsing uint: %s\n",val);
                    valu = std::stoi(std::string(val));
                    break;
                }
                case atype_double: {
                    printf("  parsing double: %s\n",val);
                    vald = std::stod(val);
                    break;
                }
                default: {
                    printf("  unkn\n");
                }
            }//switch
        }//fn-setval
    } /*Argitem*/;

    string _desc;
    Argitem _args[100];
    std::map<std::string,int> _argmap; // argname, index in _args array
    //typedef _argmap::iterator _argmapit;
    int _argslen;
    int _nreq;

    void printhelp(char* arg1)
    {
        printf("%s\n",_desc.c_str());
        printf("Usage: %s [args]\n",arg1);
        printf("args: ");
        for(int i;i<_argslen;i++){
            printf("  %s   %s\n",
                   _args[i].name.c_str(),
                   _args[i].desc.c_str()
            );
        }
    }//fn-printhelp

public:
    KArgParser():_argslen(0),_nreq(0) {}
    void add_desc(const char* description)
    {
        _desc = description;
    }
    void add_req(const char* name,const char* desc, Argtype atype)
    {
        Argitem argi;
        argi.name = std::string(name);
        argi.desc = std::string(desc);
        argi.atype = atype;
        _args[_argslen] = argi;
        _argmap[std::string(name)]=_argslen;
        _argslen+=1;
        _nreq+=1;
    }
    void add_opt(){}
    void add_flg(){}
    int parse(int ac, char** av)
    {
        printf("PARSING...\n");
        printf("Desc: %s\n",_desc.c_str());
        printf("args (n=%d,nreq=%d):\n",_argslen,_nreq);
        for(int i=0;i<_argslen;i++) {
            printf("  %s | %s\n",_args[i].name.c_str(),_args[i].desc.c_str());
        }

        // show argitem pairs
        //printf("_argmap len: %d\n",_argmap.size());
        //return -1;
        //for(auto ipair : _argmap){
        //    
        //}



        // perform parsing
        if(strcmp(av[1],"--help")==0){
            printhelp(av[0]);
            return 0;
        }

        int argind = 0;
        for(argind=0;argind<_nreq;argind++) {
            _args[argind].setval(av[argind+1]);
        }

        return 0; 
    }
    void get(const char* name,unsigned long &v)
    {
        printf("get-uint\n");
        int ind = _argmap.find(name)->second;
        printf("%s ind: %d\n",name,ind);
        assert(_args[ind].atype==atype_uint);
        v = _args[ind].valu;
        return;
    }

    void get(const char* name,double &v)
    {
        printf("get-double, %s\n",name);
        auto iname = _argmap.find(name)->first;
        std::cout << "test: " << iname << std::endl;
        //printf("here\n");
        int ind = _argmap.find(name)->second;
        printf("here2\n");
        printf("%s ind: %s, %d\n",name,iname.c_str(), ind);
        assert(_args[ind].atype==atype_double);
        v = _args[ind].vald;
        return;
    }

};

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
    ap.add_req("intensity","volume value", atype_uint);
    ap.add_req("fraction","speed factor", atype_double);
    ap.parse(argc,argv);

    unsigned long intensity;
    double fraction;
    ap.get("intensity", intensity);
    ap.get("fraction", fraction);
    printf("main scope, intensity=%lu\n",intensity);
    printf("main scope, fraction=%f\n",fraction);
    printf("done\n");
    
    return 0;
}



// eof

