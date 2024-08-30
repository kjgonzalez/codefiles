/*
https://stackoverflow.com/questions/674060/customize-cout
https://www.geeksforgeeks.org/overloading-stream-insertion-operators-c/
*/

#include <iostream>

class Log {
public:
    Log(const std::string& funcName) { std::cout << funcName << ": "; }
    template <class T>
    Log& operator<<(const T& v) {
        std::cout << v;
        return *this; // enables multiple insertion operators
    }
    ~Log() {
        //optional: run at end of object
        std::cout << " [end of message]" << std::endl;
    }
};

#define LOG_IT Log(__FUNCTION__)


int main() {
    printf("hello world 2\n");
    std::stringstream ss;

    return 0;

}


// eof
