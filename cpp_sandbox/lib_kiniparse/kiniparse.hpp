/*
kris' ini parser - a simple drop-in way to read and use INI files

* ';' and '#' are comments
* comments must be on own line, no in-line comments
* whitespace is stripped everywhere except within quotes
* sections are ignored
* allowed value types: string, int64, double

todo: 
* allow single-type array (as vector)

*/
#include <fstream>
#include <string> // read from file into buffer
#include <sstream> // to check if number
#include <map> // final object holding all key-value pairs
//#include <vector> - todo, add
#include <assert.h>

namespace kip
{
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
            enum valtype { vtype_none, vtype_int, vtype_dbl, vtype_str };
            valtype vtype;
            int64_t vi;
            double vd;
            std::string vs;
            Myval() :vtype(vtype_none), vi(-1), vd(-1.1), vs("") {}

            void parse_str(std::string rawval, bool v = false)
            {

                if (!is_numeric(rawval)) {
                    assert(rawval[0] == '"');
                    assert(rawval[rawval.size() - 1] == '"');

                    vtype = vtype_str;
                    this->vs = rawval.substr(1, rawval.size() - 2);

                    if (v) printf("'%s' set as string\n", this->vs.c_str());
                }
                else if (rawval.find('.') == -1) {
                    vtype = vtype_int;
                    this->vi = std::stoi(rawval);
                    if (v) printf("'%s' set as int\n", rawval.c_str());
                }
                else {
                    vtype = vtype_dbl;
                    this->vd = std::stod(rawval);
                    if (v) printf("'%s' set as double\n", rawval.c_str());
                }
            }
            template<typename T>
            T get()
            {

                if constexpr (std::is_same_v<T, double>)
                    return vd; // type double
                if constexpr (std::is_same_v <T, int64_t>)
                    return vi; // type int64
                if constexpr (std::is_same_v <T, std::string>)
                    return vs; // type string
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
                else if (buf.find('=') == -1) continue; // can't be eval'd for key-val pair
                //else if (buf.find('[') != -1) continue; // skip lists for now
                // otherwise, should parse

                size_t split = buf.find('=');
                auto keyraw = buf.substr(0, split);
                auto valraw = buf.substr(split + 1);
                if (valraw.find('[') != -1) continue; // skip lists for now

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


}




