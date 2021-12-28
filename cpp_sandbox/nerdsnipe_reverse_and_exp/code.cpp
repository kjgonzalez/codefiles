/*
make a program that takes a value and returns C = A^B, where A is input, B is numbers reversed. A must be within range of 0-99999

general steps:
1. take in value
2. parse, assert in range
3. reverse string, parse
4. create bigint class:
    init
    add
    prod
    pow
    print

*/

#include <iostream>
#include <vector>
#include <string>
#include <chrono> // used for milli-/micro-second timing
using namespace std;

class Stopwatch {
public:
    chrono::time_point<std::chrono::high_resolution_clock> start;
    Stopwatch(bool asap) {
        if (asap) tic();
    }
    Stopwatch() {}
    void tic() {
        start = chrono::high_resolution_clock::now();
    }

    long long tms() {
        // return elapsed time as milliseconds
        auto elapsed = chrono::high_resolution_clock::now() - start;
        return chrono::duration_cast<chrono::milliseconds>(elapsed).count();
    }
    long long tus() {
        // return elapsed time as microseconds
        auto elapsed = chrono::high_resolution_clock::now() - start;
        return chrono::duration_cast<chrono::microseconds>(elapsed).count();
    }
    void printus(string reason, bool reset = false) {
        printf("%s: %i us\n", reason.c_str(), tus());
        if (reset) tic();
    }
};



class BigInt {
    /* 
    Store very large numbers, with each decimal place being one spot in array. array is bigendian, 
    meaning that largest number is stored at end of array, e.g. BigInt[0] returns the ones place. 
    only positive values are accepted
    */

public:
    vector<int> arr;
    BigInt() {
        arr.push_back(0); // initialize value at 0
    }
    BigInt(string val) {
        set(val);
    }
    BigInt(vector<int> val) {
        set(val);
    }
    void print() {
        // print current value of array
        for (int i = arr.size() - 1; i >= 0; i--) cout << arr[i];
        cout << "\n";
    }
    void set(int val) {
        // convert given value into "current" value of object
        int rem = 0;
        int xx = val + 0;
        arr.clear();
        while (xx > 0) {
            rem = xx % 10;
            arr.push_back(rem);
            xx = (xx - rem) / 10;
        }
    }
    void set(vector<int> val) {
        arr.clear();
        for (int i = 0; i < val.size(); i++)arr.push_back(val[i]);
    }

    void set(string val) {
        // convert string of numbers into "current" value of object
        arr.clear();
        for (int i = val.length() - 1; i >= 0; i--) {
            arr.push_back((int)val[i] - '0');
        }
    }
    void set(BigInt val) {
        set(val.arr);
    }
    bool isZero() {
        // return whether current value evaluates to zero
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] != 0) return false;
        }
        return true;
    }

    long long sigs() {
        /* return how many significant figures number has */
        long long i = arr.size()-1;
        while (arr[i] == 0) i--;
        return i + 1;
    }

    bool greaterthan(BigInt val) {
        /* return whether self is greater than current value*/
        if (sigs() > val.sigs()) return true;
        if (sigs() < val.sigs()) return false;
        // otherwise, check at same starting point, going down to ones
        for (long long i = sigs() - 1; i > 0; i--) {
            if (arr[i] > val.arr[i]) return true;
            else if(arr[i] < val.arr[i]) return false;
        }//forloop
        // if get through whole loop, and no answer, then values are equal. return false.
        return false;
    }//greater than


    void sub1() {
        // subtract 1 from current value
        int rem = 1;
        int i = 0;
        while (rem == 1) {
            arr[i] -= rem;
            if (arr[i] < 0)arr[i] += 10;
            else rem = 0;
            i++;
        }//loop
    }//sub1
    void sub(long val) {
        long i = 0;
        while (i < val) {
            sub1();
            i++ ;
        }
    }
    void add(string val) {
        BigInt temp(val);
        add(temp);
    }
    void add(BigInt val) {
        int rem = 0;
        int maxit = max(val.arr.size(), arr.size());
        int i = 0;
        int ival = 0;
        bool done = false;
        int bsize = val.arr.size();
        while (not done) {
            ival = 0;
            if (i >= arr.size()) arr.push_back(0);
            if (i < bsize) ival = val.arr[i];
            rem += arr[i] + ival;
            arr[i] = rem % 10;
            rem = (rem - arr[i]) / 10;
            if (i >= bsize && rem == 0) done = true;
            i++;
        }//while-loop
    }

    void prod(string val) {
        BigInt temp(val);
        prod(temp);
    }
    void prod(BigInt val) {
        // remaking product calculation, this is likely where largest problem comes from
        vector<int> res;
        res.push_back(0);
        int rem = 0;

        int ans = 0;
        int k = 0;
        for (int i = 0; i < arr.size(); i++) {
            for (int j = 0; j < val.arr.size(); j++) {
                if (i + j >= res.size()) res.push_back(0);
                ans = rem + arr[i] * val.arr[j];
                res[i + j] += ans % 10;
                rem = (ans - (ans % 10))/10; // carry to next math operation
            }//j-loop
            if (rem != 0) {
                res.push_back(rem);
                rem = 0;
            }
            // after each top loop, sum current status of res vector
            for (int i = 0; i < res.size(); i++) {
                if (res[i] > 9 || rem != 0) {
                    ans =  (res[i]+rem) % 10; // answer for current place, e.g. 2 from 12
                    rem = (res[i]+rem - ans) / 10; // carry over for next place
                    res[i] = ans;
                }//ifstatement

            }//forloop
            if (rem != 0) {
                res.push_back(rem);
                rem = 0;
            }
        }//i-loop
        if (rem != 0) res.push_back(rem);

        // assign result to own array
        arr.clear();
        for (int i = 0; i < res.size(); i++) arr.push_back(res[i]);
    }

    void exp(int val) {
        /* 
        Take in value equal to or less than 99999 and raise arr to that power. use powers of two 
        to speed up loops 
        */

        BigInt orig(arr); // original copy
        BigInt temp; // aggregator
        int k=0;
        printf("loops remaining: ");
        set("1");
        while (val > 0) {
            temp.set(orig); // interim
            k = 1;
            while (k * 2 <= val) {
                temp.prod(temp);
                k *= 2;
            }
            prod(temp); // multiply times value
            val -= k;
            if (val == 1) {
                prod(orig);
                val--;
            }
            cout << val << ",";
        }
        cout << endl;


    }
}; // class BigInt


int main() {
    string val; // will assume don't need long
    cout << "please enter a number: ";
    cin >> val;
    string::size_type sz;
    int check = stoi(val, &sz);
    cout << "as int: " << check << endl;
    if (check < 0 || check >99999) {
        printf("ERROR! NUMBER OUT OF RANGE");
        return 0;
    } //if-inrange
    string bwd = "";
    for (int i = val.length() - 1; i >= 0; i--)bwd += val[i];
    int y = stoi(bwd);
    cout << "backward:"<< y << endl;
    Stopwatch sw(true);
    cout << "timer started \n";
    printf("%i^%i = \n", check, y);
    BigInt x(val); 
    x.exp(y);
    x.print();
    printf("time to calculate: %i [ms]\n", sw.tms());
    

    return 0;
}
