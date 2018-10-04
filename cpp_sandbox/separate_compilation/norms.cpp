/*
this file serves to define things that are declared in a header file, but should
  not be included in one. over time, this has come to mean everything, but
  traditionally (according to stroustrup, cpp_language-p425) this should be for:
    ordinary functions
    data definitions
    aggregate definitions
    unnamed namespaces (?)

*/

#include "norms.h"
#include <math.h>

double pyt(double a, double b){
  return pow(a*a+b*b,0.5);
} //pyt
