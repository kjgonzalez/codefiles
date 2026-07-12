/*

Kris' Argument Parser header-only library
  Simple arg parser as replacement for getting 3rd party library

open tasks:
todo: check that value is exactly what it should be (e.g. a fraction can be misread as an int, should raise an error)
todo: ensure equal indentation when printing args + descriptions


*/

#include <assert.h>
#include <iostream>
#include <filesystem> // only used in one place
#include <string>
#include <map>


using std::string;

enum Argtype_
{
    atype_bool,
    atype_int,
    atype_uint,
    atype_double,
    atype_str,
};
typedef enum Argtype_ Argtype;

class KArgParser
{
    struct Argitem
    {
        string name;
        string desc;
        Argtype atype;
        bool valb;
        long vali;
        unsigned long valu;
        double vald;
        string vals;
        int setval(char* val)
        {
            switch (atype) {
            case atype_bool: {
                printf("  parsing bool: %s\n", val);
                valb = (bool)std::stoi(val);
                return 0;
            }//case
            case atype_int: {
                printf("  parsing int: %s\n", val);
                if (strchr(val, '.') != NULL) return -2;
                vali = std::stoi(string(val));
                return 0;
            }//case-uint
            case atype_uint: {
                printf("  parsing uint: %s\n", val);
                if (strchr(val, '.') != NULL) return -2;
                valu = std::stoi(string(val));
                return 0;
            }//case-uint
            case atype_double: {
                printf("  parsing double: %s\n", val);
                vald = std::stod(val);
                return 0;
            }//case-double
            case atype_str: {
                printf("  parsing str: %s\n", val);
                vals = std::string(val);
                return 0;
            }//case
            default: { printf("  unkn\n"); return -1; }
            }//switch
        }//fn-setval
    };

    string _desc = "";
    Argitem _args[100]; // todo: vector
    int _argslen;
    std::map<std::string, int> _argloc; //
    int _nreq;
    bool _v;
    
    void printhelp(char* arg0_programname)
    {
        auto fname = std::filesystem::absolute(std::string(arg0_programname)).stem();
        printf("%s\n", _desc.c_str());
        printf("Usage: %s [args]\n", fname.string().c_str());
        printf("args:\n");
        for (int i=0; i < _argslen; i++) {
            printf("  %s  %s\n",
                _args[i].name.c_str(),
                _args[i].desc.c_str()
            );
        }
    }//fn-printhelp

public:
    KArgParser(bool verbose=false) :_argslen(0), _nreq(0),_v(verbose) {}
    void add_desc(const char* description) { _desc = description; }
    void add_req(const char* name, const char* desc, Argtype atype)
    {
        Argitem argi;
        argi.name = std::string(name);
        argi.desc = std::string(desc);
        argi.atype = atype;
        _args[_argslen] = argi;
        _argloc[std::string(name)] = _argslen;
        _argslen += 1;
        _nreq += 1;
    }
    void add_opt() {}
    void add_flag() {}
    int parse(int ac, char** av)
    {
        if (_v) {
            printf("PARSING...\n");
            printf("given args: \n");
            for (int i = 0; i < ac; i++) { printf("  %d: %s\n", i, av[i]); }
        }
        // perform parsing
        if (strcmp(av[1], "--help") == 0) { printhelp(av[0]); exit(0); }

        else if ((ac - 1) < _nreq) {
            printf("ERR NOT ENOUGH REQUIRED ARGUMENTS\n");
            printhelp(av[0]); exit(1);
        }


        int argind = 0;
        for (argind = 0; argind < _nreq; argind++) {
            int err = _args[argind].setval(av[argind + 1]);
            if (err) { 
                printf("ERR PARSING ARG %d (%s), EXITING\n", 
                    argind+1, av[argind+1]
                ); 
                exit(-1); 
                return -1; }
        }
        return 0;
    }
    void get(const char* name, bool& v)
    {
        if (_v) printf("get-bool\n");
        int ind = _argloc.find(name)->second;
        if (_v) printf("%s ind: %d\n", name, ind);
        assert(_args[ind].atype == atype_bool);
        v = _args[ind].valb;
    }
    void get(const char* name, long& v)
    {
        if (_v) printf("get-int\n");
        int ind = _argloc.find(name)->second;
        if (_v) printf("%s ind: %d\n", name, ind);
        assert(_args[ind].atype == atype_int);
        v = _args[ind].vali;
    }
    void get(const char* name, unsigned long& v)
    {
        if (_v) printf("get-uint\n");
        int ind = _argloc.find(name)->second;
        if (_v) printf("%s ind: %d\n", name, ind);
        assert(_args[ind].atype == atype_uint);
        v = _args[ind].valu;
    }
    void get(const char* name, double& v)
    {
        if (_v) printf("get-double\n");
        int ind = _argloc.find(name)->second;
        if (_v) printf("%s ind: %d\n", name, ind);
        assert(_args[ind].atype == atype_double);
        v = _args[ind].vald;
    }
    void get(const char* name, std::string& v)
    {
        if (_v) printf("get-str\n");
        int ind = _argloc.find(name)->second;
        if (_v) printf("%s ind: %d\n", name, ind);
        assert(_args[ind].atype == atype_str);
        v = _args[ind].vals;
    }







};//class-argparser








// eof
