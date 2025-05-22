/*

attempt to follow along: https://www.euclideanspace.com/maths/algebra/realNormedAlgebra/quaternions/code/index.htm

1. try to do basic adding and subtracting with quaternion code

*/
# pragma once

#include <ostream>
#include <string>
#include <math.h>
#define dd double

double round2(double value, int ndigits) { return (double)int(value) + round((value-int(value))*pow(10,ndigits))/pow(10,ndigits); }

class Quaternion
{
public: 
    dd w,x,y,z;
    Quaternion(dd w=0, dd x=0, dd y=0, dd z=0):w(w),x(x),y(y),z(z){}
    static Quaternion Identity(){return Quaternion(1,0,0,0); }

    std::string string() 
    {
        char buf[100]; sprintf(buf, "Quat(%.4f,%.4f,%.4f,%.4f)", w, x, y, z);
        return std::string(buf);
    }
    double norm2() { return sqrt(w*w+x*x+y*y+z*z); }
    Quaternion conjugate(){return Quaternion(w,-x,-y,-z); }
    Quaternion divideby(double value) { return Quaternion (w/value,x/value,y/value,z/value); }
    Quaternion normalize() { return Quaternion(w/norm2(),x/norm2(),y/norm2(),z/norm2()); }

};

typedef Quaternion quat;

std::ostream& operator<<(std::ostream& os, Quaternion& q) { os << q.string(); return os; }
quat operator+(const quat& p,const quat& q) {
    return quat(p.w+q.w,p.x+q.x,p.y+q.y,p.z+q.z); // test, see which is considered second
}
quat operator*(const quat& p,const quat& q)
{
    return quat(
        p.w*q.w - (p.x*q.x + p.y*q.y + p.z*q.z),
        p.w*q.x +  p.x*q.w + p.y*q.z - p.z*q.y,
        p.w*q.y -  p.x*q.z + p.y*q.w + p.z*q.x,
        p.w*q.z +  p.x*q.y - p.y*q.x + p.z*q.w
        );
}




// eof
