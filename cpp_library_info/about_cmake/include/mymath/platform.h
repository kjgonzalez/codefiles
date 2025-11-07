/*
*/

#pragma once

#ifdef _WIN32
    #define FNC extern "C" __declspec(dllexport)
    #define CLS __declspec(dllexport)
#else
    #define FNC extern "C"
    #define CLS
#endif
