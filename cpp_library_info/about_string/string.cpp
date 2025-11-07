/*
About the string library
*/

#include <string>
#include <vector> // only needed for string split

void str_replace(std::string& str, const char* old_, const char* new_, int32_t count = -1) {
    /* 
    Replace 'count' occurrences of a substring in a string. if count is -1, replace all occurrences
    */

    size_t pos = str.find(old_);
    std::string old = old_;
    while (pos != std::string::npos && count!=0) {
        str.replace(pos, old.size(), new_);
        count -= 1;
        pos = str.find(old_);
    }
}

std::vector<std::string> str_split(std::string& str, const char* delimiter) {
    /* Split a string into substrings, return vector */
    uint32_t p0=0;
    uint32_t p1=0;
    std::vector<std::string> out;
    int len_delim = std::string(delimiter).size();
    while (p1 < str.size()) {
        p1 = str.find(delimiter, p0);
        out.push_back(str.substr(p0, p1 - p0));
        p0 = p1+len_delim;
    }
    return out;
}

// nothing built-in for lower/upper, so have a few options, all around "std::tolower/toupper"
inline std::string str_lower(std::string input)
{
    std::string s = "";
    for(int i=0;i<input.length();i++)
        s+=std::tolower(input[i]);
    return s;
}

inline std::string str_upper(std::string input)
{
    std::string s = "";
    for(int i=0;i<input.length();i++)
        s+=std::toupper(input[i]);
    return s;
}

void str_upper_inplace(std::string& input)
{
    for(int i=0;i<input.length();i++)
        input[i]=std::toupper(input[i]);
}

void str_functions()
{
    // a little about how the various functions of std::string work
    std::string s;
    // about memory / availability
    // keep in mind that a string is a special kind of vector. so, some behaviors are shared between the two. 
    auto x = s.capacity(); // 15
    auto y = s.size();     // 0
    s.reserve(128);
    x = s.capacity();   // 128+15
    y = s.size();       // 0
    s.resize(256);
    x = s.capacity();   // 256+15
    y = s.size();       // 256
    /* what happened? reserve & capacity are the heap memory allocated for the object, what the 
        object is prepared to hold, and happens in the background. on the other hand, resize & 
        size describe the size of the user-accessible string. it's the difference between having 
        a large warehouse (capacity) and a lot of goods (size)
    */



}


int main() {
    std::string text = "hello world";
    printf("%s (len: %d or %d)\n", text.c_str(),text.size(),text.length());
    std::string s2;
    s2 += "this ";
    s2 += "is ";
    s2 += "a test";
    
    printf("%s ('is' at %d)\n", s2.c_str(),s2.find("is",0));
    str_replace(s2, "is", "blah",1);
    printf("result: %s\n", s2.c_str());
    std::string sample = "this is not a test";
    for (std::string istr : str_split(sample, " ")) {
        printf(">> %s\n", istr.c_str());
    }

    // test: tolower
    using std::string;

    string s3 = "This, is A test.";
    string s3a = "";
    string s3b = "";
    printf("orig:  %s\n",s3.c_str());
    printf("lower: %s\n",str_lower(s3).c_str());
    str_upper_inplace(s3);
    printf("upper: %s\n",s3.c_str());

    return 0;
}



// eof
