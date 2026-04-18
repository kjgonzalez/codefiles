/*
sample project library example for sample cmake project
*/

#include "platform.h"

namespace mymath
{
    FNC int add(int a, int b);

    FNC float eigenCheck();

    class CLS Rect
    {
        float w;
        float h;
    public:
        Rect(float wd = 0.0f, float ht = 0.0f);
        float area();
    };



    // class Rect:
    // {
    //     float w;
    //     float h;
    // public:
    //     Rect(float wd=0.0f, float ht=0.0f):w(wd),h(ht){}
    //     float area();
    // };
        

}