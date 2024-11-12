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

std::vector <std::string> str_split(std::string& str, const char* delimiter) {
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
    return 0;
}



// eof
