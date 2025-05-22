/*
this is a test

*/

#include <iostream>
#include "quaternions.hpp"
using namespace std;
using std::cout;
using std::endl;

int main() {
    quat q1 = quat(1, 2, 3, 4) +quat(5,6,7,8);
    cout << "sum : " << q1 << endl;

    double val = 1 / sqrt(2);
    quat q2 = quat(val, val, 0, 0) * quat(val, -val, 0, 0);
    cout << "mult: " << q2 << endl;

    val = 1 / sqrt(3);
    quat q3 = quat(val, val, val, 0) * quat(val, -val, -val, 0);
    cout << "mul2: " << q3 << endl;

    quat q4(4, 2, 6, 7);
    q4 = (q4 * q4.conjugate()).divideby(pow(q4.norm2(), 2));
    cout << "q*q_conj/norm(q): " << q4 << endl;

    quat q5 = quat(4, 2, 6, 7).normalize();
    q5 = q5 * q5.conjugate();
    cout << "q*q_conj/norm(q): " << q5 << endl;


    return 0;
}

