/*
just a quick demo of "range based for loop"
src: https://en.cppreference.com/w/cpp/language/range-for

kjgnote: range-based forloops must be compiled with 2011 iso stds:
>> g++ main.cpp -std=c++11

*/


#include <iostream>
#include <vector>

int main(){
  std::cout << "hello world\n";
  std::vector<int> v;
  for(int i=0;i<5;i++) v.push_back(i*3);  // normal forloop
  for(int i : v) std::cout<<" "<< i;      // range-based forloop
  std::cout << "\n Length of vector: " << v.size() << "\n";
  std::cout << "\n\n";
  return 0;
}
