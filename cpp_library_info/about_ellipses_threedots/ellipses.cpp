/*
variadic argument operator: "..."
available in C, slightly different rules for cpp

Sources:
* reference: https://en.cppreference.com/w/cpp/language/variadic_arguments.html
* basic info: https://stackoverflow.com/questions/599744/what-does-the-three-dots-in-the-parameter-list-of-a-function-mean

*/

#include <stdio.h> //printf
#include <stdarg.h> // "..." enabling

void fn(const char *input,...)
{
    va_list parg;
    const char* s;
    va_start(parg,input);
    printf("%s ",input);
    const char *ivar= va_arg(parg, const char *);
    while(ivar!=NULL){
        printf("%s ",ivar);
        ivar= va_arg(parg, const char *);
    }
    printf("\n");
    va_end(parg);
}

int main()
{
    //printf("hi\n");
    fn("this","is","a","test",NULL);
    return 0;
}
