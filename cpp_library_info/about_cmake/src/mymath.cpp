/*

*/
#include "mymath/mymath.h"
#include "Eigen/Dense" // include in... *.h=public, *.cpp=private

namespace mymath
{
    FNC int add(int a, int b) {return a+b;}

    FNC float eigenCheck() {
        Eigen::Vector3f v(2, 2, 9);
        v += Eigen::Vector3f(1, 2, 3);
        return v.norm();
    }

    Rect::Rect(float wd, float ht) :w(wd), h(ht) {}
    float Rect::area() { return w * h; }

} // mymath
// eof
