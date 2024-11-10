/*
basics of file I/O, with library fstream. WILL ALSO COMPARE WITH C APPROACH: FOPEN

include: 
* write string to a file
* write bytes to a file
* read a file

notes: 
* "fstream" is a unified, combined way of initializing read & write variables

sources: 
* c-fopen: https://cplusplus.com/reference/cstdio/fopen/
* 

*/

#define _CRT_SECURE_NO_WARNINGS //override issues with c-fileops
//#include <iostream>
#include <fstream>

void c_read_write() {
    // C approach ================================
    FILE* fptr;
    char buf[200];

    // c-style write
    fptr = fopen("tmp.txt", "wb"); // DO NOT FORGET BINARY FLAG
    for (int i = 0; i < 200; i++) buf[i] = 0;
    for (int i = 0; i < 100; i++) buf[i] = i;
    fwrite(&buf, 1, 100, fptr);
    fclose(fptr);

    // c-style read
    fptr = fopen("tmp.txt", "rb"); // DO NOT FORGET BINARY FLAG
    for (int i = 0; i < 200; i++) buf[i] = 0;
    char tmp;
    int i = 0;
    while (fread(&tmp, 1, 1, fptr) != NULL) {
        buf[i] = tmp;
        i++;
        printf("%hhx ", tmp);
    }
    printf("\n done.\n");
    fclose(fptr);
}

void cpp_read_write() {
    // C++ approach ==============================
    std::fstream f;
    // options: in, out=write, binary, ate=at end, app=append, trunc=truncate [bitwise combine]
    f.open("tmp.txt", std::fstream::out);
    f << "text\n";
    // binary
    for (char i = 0; i < 60; i++) {
        f << i; // without binary flag, just write numbers
    }

    char test[] = "this is a test";
    // can also use function to write, slightly preferable as well
    f.write(test, sizeof(test)-1); // '-1' because of null-terminated c-string
    f.close();

    char ival;
    f.open("tmp.txt", std::fstream::in | std::fstream::binary); //BINARY FLAG REQUIRED ON READ
    while (!f.eof()) {
        f.read(&ival, 1); // single char variable for demo purposes
        printf("%hhx ", ival);
    }
    f.close();
    printf("\n");
    printf("cpp read/write\n");
}

int main(){
    cpp_read_write();

    // C++ approach ==============================
    //std::fstream f;
    //// options: in, out, binary, ate=at end, app=append, trunc=truncate [combine these bitwise]
    //f.open("tmp.txt", std::fstream::out);

    ////f << "some\n";
    ////char x[100] = "text\n";
    ////f.write(x,5); // c-strings include a sentinel value, NULL (end of string)
    //// note: even when not specified, can write binary data to file
    //char x[100];
    //for (int i = 0; i < 100; i++) x[i] = i;
    //f.write(x, sizeof(x));
    //f.close();
    //
    //// read a file
    //f.open("tmp.txt",std::fstream::in);
    //char tmp;
    //for(int i = 0; i < 100; i++) x[i] = 0; // clear c-string
    //for (int i = 0; i < 100; i++) {
    //    f.read(&tmp, 1); // give addr. to tmp
    //    x[i] = tmp;
    //    //printf("%hhx ", tmp);
    //}
    //f.close();
    ////f.read(x, sizeof(x) - 1);
    ////printf("%s\n", x );


    return 0;
}




// eof