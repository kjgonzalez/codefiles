/*
mini sandbox to test things. add / remove as necessry
*/

#include <iostream>
#include <vector>
#include <stdio.h>
#include <fstream>

using namespace std;

int main(){
  // WANT TO BE ABLE TO READ IN A FILE WITH STDIO...

    FILE * pFile;
   long lSize;
    char * buffer;
    size_t result;

    pFile = fopen ( "file.txt" , "r" );
    if (pFile==NULL) {fputs ("File error",stderr); exit (1);}

    // obtain file size:
    fseek (pFile , 0 , SEEK_END);
    lSize = ftell (pFile);
    rewind (pFile);

    // allocate memory to contain the whole file:
    buffer = (char*) malloc (sizeof(char)*lSize);
    if (buffer == NULL) {fputs ("Memory error",stderr); exit (2);}

    // string line;
    // getline(pFile,line)
    // copy the file into the buffer:
    result = fread (buffer,1,lSize,pFile);
    if (result != lSize) {fputs ("Reading error",stderr); exit (3);}

    /* the whole file is now loaded in the memory buffer. */

    // terminate
    string raw=buffer;
    
    cout << buffer;
    fclose (pFile);
    free (buffer);

    return 0;
}
