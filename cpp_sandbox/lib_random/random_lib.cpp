/*
date: 200207
objective: demonstrate an easy way to use the (a?) random library
*/
#include <iostream>
#include <random>

using namespace std;

//defining stuff at the bottom to get to the code asap
float mean(vector<int> &vec);
int min(vector<int> &vec);
int max(vector<int> &vec);

void use_random_device(){
    random_device rd; // random_device should only be used to seed srand
    cout << "a random number: " << rd() << std::endl;
    cout << "max value possible:" << rd.max() << std::endl;

    cout << "Can also use this to generate a decimal value: ";
    cout << ((double)(rd()%1000000)) / (double)(1e6) << endl;

}

void use_basics(){
    // const auto epoch = std::chrono::system_clock::now().time_since_epoch();
    // const auto seconds = std::chrono::duration_cast<std::chrono::seconds>(epoch);

    random_device rd;
    srand(rd());
    cout << "random: " << rand() << endl;
}

int main (){
    use_random_device();
    use_basics();
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
