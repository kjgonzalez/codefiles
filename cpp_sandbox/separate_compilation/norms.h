/*
here, will declare a function, but then specifically define it in an
  identically named cpp function, which is the conventional approach

this is done by linking things together, aka by including all cpp files in
  the compilation command
*/

#ifndef NORMS_H
#define NORMS_H
/*
the above lines are called "include guards", and are described in
  cpp_language,p441. note, last sentence: "headers should be included only
  when necessary"
*/

double pyt(double a, double b);


#endif
