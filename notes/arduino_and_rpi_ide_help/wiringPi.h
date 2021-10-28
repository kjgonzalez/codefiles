#pragma once

/* 
THIS HEADER LIBRARY EXISTS ONLY AS AN APPROXIMATION OF THE REAL 
    WIRING PI, WHICH CAN ONLY BE COMPILED ON A RASPBERRY PI 
*/

#include <iostream>
#pragma warning(disable : 4996) // disable time warning, this warning only exists in visual studio
#include <chrono>
#include <time.h>

constexpr int INT_EDGE_FALLING = 0;
constexpr int INT_EDGE_RISING = 1;
constexpr int INT_EDGE_BOTH = 2;
constexpr int INPUT = 1;
constexpr int OUTPUT = 1;
constexpr int LOW = 0;
constexpr int HIGH = 1;
auto time0 = std::chrono::high_resolution_clock::now();


void delayMicroseconds(unsigned int howLong) {
  // advanced sleep a given number of seconds, using chrono
  long long asuS = (long long)(howLong);
  auto start = std::chrono::high_resolution_clock::now();
  auto elapsed = std::chrono::high_resolution_clock::now() - start;
  long long microseconds = std::chrono::duration_cast<std::chrono::microseconds>(elapsed).count();
  while (microseconds < asuS) { 
    elapsed = std::chrono::high_resolution_clock::now() - start;
    microseconds = std::chrono::duration_cast<std::chrono::microseconds>(elapsed).count();
  }
}

void delay(unsigned int howLong) {
  // advanced sleep a given number of seconds, using chrono
  delayMicroseconds(1000 * howLong);
}

void wiringPiSetupGpio() { 
    std::printf("gpio setup\n"); 
    time0 = std::chrono::high_resolution_clock::now(); // start timer when gpio is initialized

};

void pinMode(int pin, int state) { std::printf("pinMode: pin %d set to %d\n",pin,state); };

void wiringPiISR(int pin, int edge, void function(void)) { std::printf("ISR setup\n"); };

void digitalWrite(int pin, int state) { std::printf("digitalWrite: pin %d set to %d\n",pin, state); };

int digitalRead(int pin) { return 1; };

unsigned int millis() { 
    auto elapsed = std::chrono::high_resolution_clock::now() - time0;
    return (unsigned int) std::chrono::duration_cast<std::chrono::milliseconds>(elapsed).count();
};


