/*
objectives:
1. compile exclusively c (not c++) with cmake
    CONFIRMED: with current config, c++ not able to compile (msvc 17, cmake as-is)
2. import interesting stdint.h (c header) that allows specific size guarantees of primitives
    CONFIRMED: possible with c, added in C99 (so, effectively part of modern C)
*/

#include <stdio.h> // only for printf
#include <stdint.h> // allows specifying guaranteed primitive sizes in c

int main() {
    printf("hi\n");
    uint16_t u16 = 23;
    printf("sizeof(uint8_t): %llu\n", sizeof(uint8_t)); // 1
    printf("sizeof(uint16): %llu\n", sizeof(u16));      // 2
    printf("sizeof(wchar_t): %llu\n", sizeof(wchar_t)); // 2
    return 0;
}
