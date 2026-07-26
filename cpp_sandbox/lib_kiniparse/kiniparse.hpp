/*
Kris' Ini File Parser header-only library- a simple drop-in way to read and use INI files

* ';' and '#' are comments
* comments must be on own line, no in-line comments
* whitespace is stripped everywhere except within quotes
* sections are ignored
* allowed value types: string, int64, double, list of previous

*/
#include <assert.h> // minor asserts
#include <fstream>  // open file
#include <string>   // read from file into buffer
#include <sstream>  // to check if number
#include <map>      // final object holding all key-value pairs
#include <vector>   // parse lists

class IniParse
{
    void trim_for_ini(std::string& s)
    {
        int i = 0;
        bool inquotes = false; // don't remove whitespace from within quotes
        while (i < s.length())
        {
            if (s[i] == '"') inquotes = !inquotes; // todo
            if (s[i] == ' ' && !inquotes) s = s.replace(s.begin() + i, s.begin() + i + 1, "");
            else i++;
        }
    }

    class Myval
    {
        bool is_numeric(std::string raw)
        {
            std::stringstream ss;
            ss << raw;
            double f = 0;
            ss >> f;
            if (ss.good() || (f == 0 && raw[0] != '0')) return false;
            return true;
        }
    public:
        enum valtype { vtype_none, vtype_int, vtype_dbl, vtype_str,vtype_listint, vtype_listdbl, vtype_liststr };
        enum valtype vtype;
        int64_t vi;
        double vd;
        std::string vs;
        std::vector<int64_t> veci;
        std::vector<double> vecd;
        std::vector<std::string> vecs;
        Myval() :vtype(vtype_none), vi(-1), vd(-1.1), vs("") {}

        enum valtype parse_type(std::string& s, bool v = false)
        {
            if (s[0] == '[' && s[s.size() - 1] == ']' && s.find('"') != -1) return vtype_liststr;
            else if (s[0] == '[' && s[s.size() - 1] == ']' && s.find('.') != -1) return vtype_listdbl;
            else if (s[0] == '[' && s[s.size() - 1] == ']') return vtype_listint;
            else if (!is_numeric(s) && s[0] == '"' && s[s.size() - 1] == '"') return vtype_str;
            else if (is_numeric(s) && s.find('.') != -1) return vtype_dbl;
            else if (is_numeric(s)) return vtype_int;
            return vtype_none;
        }

        void parse_list(std::string& s, bool v = false)
        {
            size_t p0 = 0;
            size_t p1 = 0;
            // determine type of first, set for all
            while (p1 < s.size()) {
                p1 = s.find(',', p0);
                if (vtype == vtype_listint) {
                    veci.push_back( std::stoi(s.substr(p0,p1-p0)) );

                }
                else if (vtype == vtype_listdbl) {
                    vecd.push_back( std::stod(s.substr(p0, p1-p0)) );
                }
                else { // vtype==vtype_liststr
                    if (p1 == -1) p1 = s.size(); // deal with quotation marks & string length
                    vecs.push_back( s.substr(p0+1,p1-p0-2) );
                }
                p0 = p1 + 1;
            }//while
        }//parse_list

        void parse_str(std::string& rawval, bool v = false)
        {
            vtype = parse_type(rawval, v);
            switch (vtype) {
            case(vtype_int):
                this->vi = std::stoi(rawval);
                if (v) printf("'%s' set as int\n", rawval.c_str());
                break;
            case(vtype_dbl):
                this->vd = std::stod(rawval);
                if (v) printf("'%s' set as double\n", rawval.c_str());
                break;
            case(vtype_str):
                this->vs = rawval.substr(1, rawval.size() - 2);
                if (v) printf("'%s' set as string\n", this->vs.c_str());
                break;
            case(vtype_listint):
                parse_list(rawval.substr(1,rawval.size()-2), v);
                if (v) printf("'%s' set as int list\n", rawval.c_str());
                break;
            case(vtype_listdbl):
                parse_list(rawval.substr(1, rawval.size() - 2), v);
                if (v) printf("'%s' set as double list\n", rawval.c_str());
                break;
            case(vtype_liststr):
                parse_list(rawval.substr(1, rawval.size() - 2), v);
                if (v) printf("'%s' set as string list\n", rawval.c_str());
                break;
            default:
                printf("INVALID TYPE DETECTED\n");
                assert(vtype != vtype_none);
            }//case
        }//parse_str
        template<typename T>
        T get()
        {
            if constexpr (std::is_same_v <T, int64_t>)
                return vi;
            if constexpr (std::is_same_v<T, double>)
                return vd;
            if constexpr (std::is_same_v <T, std::string>)
                return vs;
            if constexpr (std::is_same_v <T, std::vector<int64_t>>)
                return veci;
            if constexpr (std::is_same_v < T, std::vector<double>>)
                return vecd;
            if constexpr (std::is_same_v < T, std::vector<std::string>>)
                return vecs;
            printf("ERR invalid value dtype\n");
            throw 1;
        }
    };

    std::map<std::string, Myval> d;
    bool is_parsed = false;
    bool verbose = false;


public:
    IniParse(bool verbose_ = false) :is_parsed(false), verbose(verbose_) {}

    //load and parse INI config file
    int load(const char* path)
    {
        std::ifstream fin;
        std::string buf;
        fin.open(path);
        while (!fin.eof()) {
            std::getline(fin, buf); // note: strips out end of line (\n or \r\n)
            trim_for_ini(buf);
            if (buf.size() == 0) continue;
            else if (buf[0] == ';' || buf[0] == '#') continue;
            else if (buf[0] == '[') continue; // skip sections for now
            else if (buf.find('=') == -1) continue; // can't be evaluated for key-val pair
            //else if (buf.find('[') != -1) continue; // skip lists for now
            // otherwise, should parse

            size_t split = buf.find('=');
            auto keyraw = buf.substr(0, split);
            auto valraw = buf.substr(split + 1);
            //if (valraw.find('[') != -1) continue; // skip lists for now

            d[keyraw] = Myval();
            d[keyraw].parse_str(valraw, verbose);
            if (verbose) printf("PARSED: %s, %s\n", keyraw.c_str(), valraw.c_str());

        }
        fin.close();
        if (verbose) printf("parsing complete\n");
        return 0;
    }
    template<typename T>
    T get(std::string key) { return d[key].get<T>(); }
};

