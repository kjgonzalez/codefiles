/*
how to use the vector library
*/

#include <vector>


int main() {
    int x = 2;
    int y = sizeof(x);
    
    std::vector<int> v; // initialization method 1
    v.push_back(2);
    v.push_back(3);
    v.insert(v.begin(),1); // insert at 0
    v.insert(v.begin()+2, 7); // insert at 2 => [1,2,7,3]

    std::vector<int> w = { 2,3,4,5 }; // initialization method 2

    std::vector<int> u[10]; // initialization method 3

    // normal forloop
    for (int i = 0; i < v.size(); i++) printf("%d ", v[i]);
    printf(". ");
    // foreach: 
    for (int ival : v) printf("%d ", ival);
    printf("\n");

    v.erase(v.begin()+2); // need to offset from begin or end

    //reverse the vector
    std::reverse(v.begin(), v.end()); //note: reverse part of vector lib

    return 0;
}

// eof