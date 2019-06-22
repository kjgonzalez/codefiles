/*
author: kris gonzalez
date: 190618
objective: do some stuff with vectors to help yourself understand them.

compile: g++ -std=c++11 vectors.cpp
*/

#include <iostream>
#include <algorithm>
#include <vector>
#define nl '\n'

void vPrint(std::vector<int> myvect){
    for(int i=0;i<myvect.size();i++){
        std::cout << myvect[i] << " ";
    }
    std::cout<< "\n";
}


int main(){
    std::vector<int> first;
    first.assign(7,100);
    std::vector<int>::iterator it;
    int myints[]={1776,7,4};
    std::cout<<"Size of first: " << int (first.size()) << '\n';
    std::cout << "first contents: "; vPrint(first);

    for(int i=0;i<first.size();i++) first[i]=i+3;
    std::cout << "new first contents: "; vPrint(first);

    std::vector<int> second;
    it=first.begin()+1;
    second.assign (it,first.end()-1); // the 5 central values of first
    std::cout << "second contents: "; vPrint(second);

    // int x = std::max_element(first.begin(),first.end());
    // printf("max value: %d\n",x);
    std::cout << "max value: " << *std::min_element(first.begin(),first.end()) << nl;

    // for(int i=0;i<first.size();i++){
    //     std::cout << first[i] << " ";
    // }//forloop
    // printf("\n");

    // printf("first.begin: ");
    // std::cout << first.begin() << nl;
}//main
