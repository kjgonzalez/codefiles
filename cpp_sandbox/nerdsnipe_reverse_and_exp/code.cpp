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
using namespace std;

class BigInt{
    /* store very large numbers, with each decimal place being one spot in array. array is bigendian, meaning that largest number is stored at end of array, e.g. BigInt[0] returns the ones place. only positive values are accepted*/
    
public:
    vector<int> arr;
    BigInt(){
        arr.push_back(0); // initialize value at 0
    }
    BigInt(string val){
        set(val);
    }
    BigInt(vector<int> val){
        set(val);
    }
    void print(){
        // print current value of array
        for(int i=arr.size()-1;i>=0;i--) cout << arr[i];
        cout << "\n";
    }
    void set(int val){
        // convert given value into "current" value of object
        int rem=0;
        int xx=val+0;
        arr.clear();
        while(xx > 0){
            rem = xx%10;
            arr.push_back(rem);
            xx = (xx-rem)/10;
        }
    }
    void set(vector<int> val){
        arr.clear();
        for(int i=0;i<val.size();i++)arr.push_back(val[i]);
    }

    void set(string val){
        // convert string of numbers into "current" value of object
        arr.clear();
        for(int i=val.length()-1;i>=0;i--) {
            arr.push_back( (int)val[i]-'0' );
        }
    }
    bool isZero(){
        // return whether current value evaluates to zero
        for(int i=0;i<arr.size();i++){
            if(arr[i]!=0) return false;
        }
        return true;
    }
    void sub1(){
        // subtract 1 from current value
        if(isZero()) return;
        int rem=1;
        int i=0;
        while(rem==1){
            arr[i]-=rem;
            if(arr[i]<0)arr[i]+=10;
            else rem=0;
            i++;
        }//loop
    }//sub1
    
    void add(BigInt val){
        int rem = 0;
        int maxit = max(val.arr.size(),arr.size());
        for (int i=0;i<maxit;i++){
            if(i>=arr.size())arr.push_back(0);
            rem +=arr[i];
            if(i<val.arr.size()) rem+=val.arr[i];
            arr[i]=rem%10;
            rem=(rem-arr[i])/10;
        }
        // if something still remains, add it up
        if(rem!=0) arr.push_back(rem);
    }
    
    void prod(BigInt val){
        BigInt orig(arr);
        val.sub1();
        while(!val.isZero()) {
            add(orig);
            val.sub1();
        }
    }
    
    void exp(BigInt val){
        BigInt b;
        b.set(arr);
        val.sub1();
        while(!val.isZero()){
            prod(b);
            val.sub1();
        }//loop
    }

}; // class bigint


int main(){
    string val; // will assume don't need long
    cout << "please enter a number: ";
    cin >> val;
    string::size_type sz;
    int check = stoi(val,&sz);
    cout << "as int: " << check << endl;
    if(check<0 || check >99999){
        printf("ERROR! NUMBER OUT OF RANGE");
        return 0;
    }
    string bwd="";
    for(int i =val.length()-1;i>=0;i--)bwd+=val[i];
    cout << "backward:"<<bwd << endl;
    BigInt x(val);
    BigInt y(bwd);
    x.exp(y);
    printf("Result: %s^%s is\n",val.c_str(),bwd.c_str());
    x.print();
    
    
    // want to take modulus and keep dividing.
    return 0;
}
