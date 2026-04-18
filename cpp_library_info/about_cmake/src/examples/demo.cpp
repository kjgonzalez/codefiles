/*

*/

#include <iostream>
#include "mymath/mymath.h"

int main()
{
    printf("about_cmake demo\n");
    printf("fnc sum: %d\n", mymath::add(3, 4));
    mymath::Rect r(3, 4);
    printf("cls rect(3,4).area: %f\n",r.area());
    printf("lib eigen check: %f \n", mymath::eigenCheck());

    return 0;
}