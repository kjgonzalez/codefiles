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
    int maxx(int a, int b) {return (a>b) ? a : b;}
    struct Argitem
    {
        // attributes
        string name;
        string desc;
        Argtype atype;
        bool valb;
        long vali;
        unsigned long valu;
        double vald;
        string vals;
        //
        bool _isopt;
        // methods
        std::string as_str()
        {
            if(atype==atype_bool) return std::to_string(valb);
            else if(atype==atype_int) return std::to_string(vali);
            else if(atype==atype_uint) return std::to_string(valu);
            else if(atype==atype_double) return std::to_string(vald);
            else return vals;
        }
        int setval(char* val,bool _ver=false)
        {
            switch (atype) {
            case atype_bool: {
                if(_ver) printf("  parsing bool: %s\n", val);
                valb = (bool)std::stoi(val);
                return 0;
            }//case
            case atype_int: {
                if (_ver) printf("  parsing int: %s\n", val);
                if (strchr(val, '.') != NULL) return -2;
                vali = std::stoi(string(val));
                return 0;
            }//case-uint
            case atype_uint: {
                if (_ver) printf("  parsing uint: %s\n", val);
                if (strchr(val, '.') != NULL) return -2;
                valu = std::stoi(string(val));
                return 0;
            }//case-uint
            case atype_double: {
                if (_ver) printf("  parsing double: %s\n", val);
                vald = std::stod(val);
                return 0;
            }//case-double
            case atype_str: {
                if (_ver) printf("  parsing str: %s\n", val);
                vals = std::string(val);
                return 0;
            }//case
            default: { if (_ver) printf("  unkn\n"); return -1; }
            }//switch
        }//fn-setval
    };

    string _desc = "";
    Argitem _args[100]; // todo: vector
    int _argslen;
    std::map<std::string, int> _argloc;
    int _nreq;
    bool _v;

    void printhelp(char* arg0_programname)
    {
        int _nopt=_argslen-_nreq;
        int _nchars=0; // offset for nice printing
        for (int i=0; i < _argslen; i++) {
            if(_args[i]._isopt) _nchars = maxx(_nchars,_args[i].name.length()+2);
            else _nchars = maxx(_nchars,_args[i].name.length());
        }
        _nchars +=4; // account for small offset & spacing
        auto fname = std::filesystem::absolute(
                std::string(arg0_programname)).stem();
        printf("%s\n", _desc.c_str());
        printf("Usage: %s [args]\n", fname.string().c_str());
        
        // required arguments
        if(_nreq>0) printf("required:\n");
        int ii=0;
        for(ii=0;ii<_nreq;ii++){
            printf("  %s",_args[ii].name.c_str());
            for(int j=_args[ii].name.length()+2;j<_nchars;j++) printf(" ");
            printf("%s\n",_args[ii].desc.c_str());
        }

        // optional arguments
        printf("optional:\n");
        for (; ii<_argslen; ii++) {
            printf("  --%s",_args[ii].name.c_str());
            for(int j=_args[ii].name.length()+4;j<_nchars;j++) printf(" ");
            printf("%s ",_args[ii].desc.c_str());
            std::cout << "[default:" << _args[ii].as_str() << "]\n";
        }
    }//fn-printhelp

public:
    KArgParser(bool verbose = false) :_v(verbose) { reset(); }
    void add_desc(const char* description) { _desc = description; }
    void add_req(const char* name, const char* desc, Argtype atype)
    {
        assert(_nreq==_argslen); // ensure that not adding req after an opt
        Argitem argi;
        argi._isopt=false;
        argi.name = std::string(name);
        argi.desc = std::string(desc);
        argi.atype = atype;
        _args[_argslen] = argi;
        _argloc[std::string(name)] = _argslen;
        _argslen += 1;
        _nreq += 1;
    }

    // add an optional argument. for bools, it's recommended to use "add_flag"
    template<typename T>
    void add_opt(const char* name, const char* desc, T defaultval)
    {
        Argitem argi;
        argi._isopt=true;
        argi.name = std::string(name);
        argi.desc = std::string(desc);
        if constexpr (std::is_same<T, bool>::value) { 
            argi.atype = atype_bool; argi.valb = defaultval; }
        else if constexpr (std::is_same<T, int64_t>::value) { 
            argi.atype = atype_int; argi.vali = defaultval; }
        else if constexpr (std::is_same<T, uint64_t>::value) { 
            argi.atype = atype_uint; argi.valu = defaultval; }
        else if constexpr (std::is_same<T, double>::value) { 
            argi.atype = atype_double; argi.vald = defaultval; }
        else if constexpr (std::is_same<T, string>::value) { 
            argi.atype = atype_str; argi.vals = defaultval; }
        else { assert(0 == 1); /*return -1;*/ }
        _args[_argslen] = argi;
        _argloc[std::string(name)] = _argslen;
        _argslen += 1;
    }

    // add optional argument for booleans
    void add_flag(const char* name, const char* desc, bool defaultval)
    {
        Argitem argi;
        argi._isopt=true;
        argi.name = std::string(name);
        argi.desc = std::string(desc);
        argi.atype = atype_bool;
        argi.valb = defaultval;
        _args[_argslen] = argi;
        _argloc[std::string(name)] = _argslen;
        _argslen += 1;
    }

    template<typename T>
    T get(const char* name)
    {
        auto res = _argloc.find(name);
        if (res == _argloc.end()) {
            printf("ERR KEY NOT FOUND (%s), EXITING\n", name);
            exit(-7);
        }
        int ind = res->second;
        if constexpr (std::is_same<T, bool>::value) { return _args[ind].valb; }
        else if constexpr (std::is_same<T, int64_t>::value) { 
            return _args[ind].vali; }
        else if constexpr (std::is_same<T, uint64_t>::value) { 
            return _args[ind].valu; }
        else if constexpr (std::is_same<T, double>::value) { 
            return _args[ind].vald; }
        else if constexpr (std::is_same<T, string>::value) { 
            return _args[ind].vals; }
        else { assert(0 == 1); return -1; }
    }//fn-get

    int parse(int ac, char** av)
    {
        if (_v) {
            printf("PARSING...\n");
            printf("given args: \n");
            for (int i = 0; i < ac; i++) { printf("  %d: %s\n", i, av[i]); }
        }
        // check for easy errors
        if (ac>1 && strcmp(av[1], "--help") == 0) { printhelp(av[0]); exit(0); }
        else if ((ac - 1) < _nreq) {
            printf("ERR NOT ENOUGH REQUIRED ARGUMENTS, EXITING\n");
            printhelp(av[0]); exit(-1);
        }
        // regular parsing attempt
        int argind = 0;
        // required arguments
        for (argind = 0; argind < _nreq; argind++) {
            int err = _args[argind].setval(av[argind + 1]);
            if (err) {
                printf("ERR PARSING REQ'D ARG %d (%s), EXITING\n", 
                        argind + 1, av[argind + 1]);
                printhelp(av[0]); exit(-2);
            }
        }//for-required
        // optional / flag arguments
        for (; argind < ac-1; argind++) {
            if (av[argind + 1][0] != '-' && av[argind + 1][1] != '-') {
                printf("ERR PARSING OPTIONAL ARG %d (%s), EXITING\n", 
                        argind + 1, av[argind + 1]);
                printhelp(av[0]); exit(-3);
            }
            string baseargname = std::string(av[argind + 1]).substr(2);
            auto res = _argloc.find(baseargname);
            if (res == _argloc.end()) {
                printf("ERR PARSING OPTIONAL ARG %d (%s), EXITING\n", 
                        argind + 1, av[argind + 1]);
                printhelp(av[0]); exit(-4);
            }
            int ind = res->second;
            // is "optional" argument
            if (_args[ind].atype != atype_bool) {
                if (argind + 2 >= ac) {
                    printf("ERR NOT ENOUGH OPTIONAL ARGUMENTS, EXITING\n");
                    printhelp(av[0]); exit(-5);
                }
                if (_v) printf("argind = %d, a=%s, b=%s, ind=%d\n", 
                        argind, av[argind + 1], av[argind + 2], ind);
                int err = _args[ind].setval(av[argind + 2]);
                argind++; // move forward extra index, optional arg uses 2 indices
                if (err) {
                    printf("ERR PARSING OPTIONAL ARG %d (%s), EXITING\n", 
                            argind + 2, av[argind + 2]);
                    printhelp(av[0]); exit(-6);
                }
            }//if-NOT-atypebool
            // is "flag" argument
            else {
                if (_v) printf("argind = %d, a=%s, ind=%d\n", 
                        argind, av[argind + 1], ind);
                _args[ind].valb = !_args[ind].valb;
            }
        } // for-optionals
        return 0;
    } // fn-parse

    void reset()
    {
        _argslen = 0;
        _nreq = 0;
    }



};//class-argparser








// eof
