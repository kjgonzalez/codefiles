/*
attempts to use c strings 

notes: 
* c-strings must be null terminated. if they arent, they become invalid and dangerous
* strlen only checks where first 0x0 is
* strcat appends the second string to the first. e.g. strcat(s1,s2) -> s2 has all info
* strcat would ideally use a character array with sufficient memory allocated



* pass a string into a function - done
* return a string from a function - done
* concatenate two strings - done
* insert a value into a string - this is a self made function

*/

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

typedef unsigned int err_t;


char* strchange(char* text1, char text2[], int szt2)
{
    // will this be enough to pass in and out? 
    printf("input: %s\n", text1);
    if (szt2 < 100) return 1;
    sprintf(text2, "%s. lala", text1);
    return text2;
}



int main()
{
    printf("test\n");
 
    char* str1 = "this is a test";
    char* str2 = "another test";
    printf("%s | %s\n", str1, str2);
    
    char done = 0;
    int i = 0;
    char chr;
    char buf[1000];
    //for (int i = 0; i < 1000; i++) buf[i] = 0;
    sprintf(&buf, "%s. %s. hi", str1, str2);
    printf("len1: %zu\n", strlen(str1));
    printf("len2: %zu\n", strlen(str2));

    size_t ilen = 0;
    ilen = strlen(buf);

    buf[15] = 0;
    ilen = 0;
    ilen = strlen(buf);

    chr = buf[ilen - 1];
    chr = buf[ilen];

    char* thing = strchange(str1, buf, 1000);

    printf("%s\n", thing);

    char str3[1000];
    for (int i = 0; i < 1000; i++) str3[i] = 0;
    //char* str3 = "a";
    strcat(str3, str1);
    strcat(str3, str2);
    
    printf("strcat: %s\n", str3);

    //tmp_check();
    return 0;
}

// eof