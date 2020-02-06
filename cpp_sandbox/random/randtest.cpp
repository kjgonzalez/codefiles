/*
Author: Kris Gonzalez
DateCreated: 180527
Objective: quick show how to use a simple random number generator
src: http://www.cplusplus.com/reference/random/

note: compilation command:
g++ randtest.cpp -std=c++11
*/

#include <iostream>
#include <time.h>
#include <random>
#include <cstdlib>
// using namespace std;


int main(){
    // method 1: make it time based
    srand (time(NULL));
    std::cout << "hello world!" << std::endl;
    double a = rand()%1000;
    a = (rand()%1000);
    a=a/1000;
    // std::cout << std::itof(rand()%100) << std::endl;
    std::cout << a << '\n';

    // method 2: use random library (better)
    std::default_random_engine generator;
    std::uniform_int_distribution<int> distribution(0,9);
    std::cout << distribution(generator) << std::endl;

    // method 3, perhaps the best
    typedef std::mt19937 rng_type;
    std::uniform_int_distribution<rng_type::result_type> udist(0, 7);
    rng_type rng;

    // seed first
    // rng_type::result_type const seedval = get_seed(); // get this from somewhere
    rng.seed(0);

    rng_type::result_type random_number = udist(rng);

    std::cout << "method3: "<<random_number<<'\n';
    std::cout << "method4: " << rand()%10 << '\n';
	return 0;
}//int main
