/*
datecreated: 190709
objective: want to test out miscellaneous stuff about code

*/


#include <iostream>
#include <strings.h> // string library augmented with nonstandard functions

int main(){

    printf("res1: %d\n",strcasecmp("one","one"));
    printf("res2: %d\n",strcasecmp("one","ONE"));
    printf("res3: %d\n",strcasecmp("one","One"));
    printf("res4: %d\n",strcasecmp("one","ond"));
    printf("res5: %d\n",strcasecmp("one","onf"));
    printf("res5: %d\n",strcasecmp("one","ong"));

    printf("next, want to show what happens when you put '!' in front\n");
    printf("res1b: %d\n",!strcasecmp("one","one"));
    printf("res2b: %d\n",!strcasecmp("one","ONE"));
    printf("res3b: %d\n",!strcasecmp("one","One"));
    printf("res4b: %d\n",!strcasecmp("one","ond"));
    printf("res5b: %d\n",!strcasecmp("one","onf"));
    printf("res5b: %d\n",!strcasecmp("one","ong"));
    return 0;
}
