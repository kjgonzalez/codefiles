#include <pybind11/pybind11.h>

int myfunc(int a, int b) {return a+b;}

PYBIND11_MODULE(simple_module,cpp_interim)
{
    cpp_interim.def("myfunc",&myfunc);
}


