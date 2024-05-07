/*
Compare the performance between protobuf and flatbuffers.

key items that will be used
*/

#include <iostream>
#include <random>
#include <chrono>
#include <vector>

uint64_t micros(){
    uint64_t us = std::chrono::duration_cast<std::chrono::microseconds>(
        std::chrono::high_resolution_clock::now().time_since_epoch()).count();
    return us;
}

int main() {
    // initialize basic items for testing to standardize and control
    std::random_device rd;
    uint64_t t0;
    uint64_t t1;
    t0 = micros();
    srand(rd());
    std::vector<uint32_t> vec32;
    for (int i = 0; i < 500; i++) { 
        //std::cout << rand() << std::endl;
        vec32.push_back(rand()); 
    }
    std::vector<float> vecfloat;
    float ival;
    for (int i = 0; i < 500; i++) {
        ival = (float)(rand()) / ((float)RAND_MAX);
        //std::cout << (ival-0.5)*30 << std::endl;
        vecfloat.push_back(ival * 10);
    }
    t1 = micros();
    printf("intialization dt: %llu \n", t1 - t0);

    // create 10 flatbuffers messages



    return 0;
}


// eof
