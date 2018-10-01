/*
Author: Kris Gonzalez
DateCreated: 180527
Objective: quick show how to use a simple random number generator

note: compilation command:
g++ randtest.cpp -std=c++11
*/

#include <iostream>
// #include <stdlib.h>
#include <time.h>
// #include <random>
// using namespace std;

int main(){
	srand (time(NULL));
	std::cout << "hello world!" << std::endl;
	double a = rand()%1000;
	a = (rand()%1000);
	a=a/1000;
	// std::cout << std::itof(rand()%100) << std::endl;
	std::cout << a << '\n';
	return 0;
}//int main
