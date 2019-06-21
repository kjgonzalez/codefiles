/*
objective: understand how a silly array of vector of ints works.
*/

#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> sample[3];
    sample[0].push_back(0);
    sample[0].push_back(1);
    sample[0].push_back(2);

    sample[1].push_back(3);
    sample[1].push_back(4);
    sample[1].push_back(5);

    sample[2].push_back(6);
    sample[2].push_back(7);
    sample[2].push_back(8);

    /* | 0 1 2 |
       | 3 4 5 |
       | 6 7 8 | */

    cout << "Hello world\n";
    int arr = 2;
    int vec = 1;
    cout << "item: " << sample[arr][vec] << "\n";
    return 0;
    
}//main