/*
date: 200207
objective: demonstrate an easy way to use the random library
*/
#include <iostream>
#include <random>
#include <vector>
using namespace std;

//defining stuff at the bottom to get to the code asap
float mean(vector<int> &vec);
int min(vector<int> &vec);
int max(vector<int> &vec);

int main (){
    random_device rd;
    cout << "a random number: " << rd() << std::endl;

    cout << "kjg: at this point, will test and see what happens with 10k dice rolls" << endl;

    vector<int> v;
    for(int i=0;i<10000;i++){
        v.push_back(rd()%20+1);
    }

    cout << "average value:" << mean(v) << endl; // ~10.5
    cout << "max     value:" << max(v) << endl; // 20
    cout << "min     value:" << min(v) << endl; // 1


    return 0;
}

float mean(vector<int> &vec){
    int sum=0;
    for(int i=0;i<vec.size();i++){sum+=vec[i];}
    float m = (float)(sum) / (float)(vec.size());
    return m;
}

int max(vector<int> &vec){
    int m=0;
    for(int i=0;i<vec.size();i++){
        if(m<vec[i]){m=vec[i];}
    }
    return m;
}

int min(vector<int> &vec){
    int m=1e6;
    for(int i=0;i<vec.size();i++){
        if(m>vec[i]){m=vec[i];}
    }
    return m;
}
