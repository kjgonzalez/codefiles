/*
Author: Kris Gonzalez
DateCreated: 180529
Objective: test out some simple trigonometric functions via math library
*/

#include <iostream>
#include <math.h>
#define pi 3.14159
int main(int argc, char const *argv[]) {
	//try something out.
	float angle = pi/4;

	std::cout << sin(angle) << '\n';
	return 0;
}
