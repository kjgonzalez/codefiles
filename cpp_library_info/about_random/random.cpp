/*
random library (both c and cpp)

notes: 
* c-random best used with a good seed, such as from time
* mersenne twister generator not always needed
* to shuffle on an array (not vector), pass addr's of first/(last+1) element in array
* can seed the random number generator, but sequence is same each startup
*/

#include <random>
#include <vector> // only for demonstrating std::shuffle on vector
//#include <stdlib.h> only needed for c-random if no cpp-stdlib's are imported
#include <iostream>
int main() {
    std::random_device rd; // generates 32bit rand values (max=2^32)
    std::mt19937 g(rd()); // mersenne twister engine, for shuffling
    printf("rand: %lu\n", rd());
    printf("rmin: %lu\n", rd.min());
    printf("rmax: %lu\n", rd.max());

    std::vector<int> v = { 1,2,3,4,5,6 };
    std::shuffle(v.begin(), v.end(),g); // shuffles in-place
    for (int i : v) printf("%d ", i);
    printf("\n");

    int w[6] = { 7,8,9,10,11,12 }; // len: 6
    std::shuffle(&w[0], &w[6], g); // strangely, give index past actual array
    for (int i : w) printf("%d ", i);
    printf("\n");

    // for c-random, instead do the following, assuming <stdlib.h> is available
    //printf("max: %llu\n", RAND_MAX); // RAND_MAX seems to be 32767 (2^15) (???)

    srand(3);
    printf("c-random val: %lu\n",rand());
    printf("c-random max: %lu\n", RAND_MAX);

    return 0;
}


// eof