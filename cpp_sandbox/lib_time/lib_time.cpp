/*
 Author: Kris Gonzalez
 DateCreated: 180528
 Objective: try out some of the simple time-based operations you know.

STAT | DESCRIPTION
done | show current time
done | show elapsed time
done | pause / sleep for a certain amount of time
???? | show time as kjg standard, eg. 2020Feb06-22:08:15 >> YYYYMMMDD-HH:mm:SS

 */
#pragma warning(disable : 4996) // disable time warning
#include <iostream>
#include <string>
#include <time.h> // AKA ctime
#include <chrono> // used for milli-/micro-second timing
using namespace std; // time lib doesn't need this, but convenient

void sleep(int s){
    // basic sleep a given number of seconds, using ctime
    int t0=time(NULL);
    int t1=time(NULL)-t0;
    while(t1<s){t1=time(NULL)-t0;}
}

void sleep2(double seconds){
    // advanced sleep a given number of seconds, using chrono
    long long asMS = (long long) (1e6*seconds);
    auto start = chrono::high_resolution_clock::now();
    auto elapsed = chrono::high_resolution_clock::now() - start;
    long long microseconds = chrono::duration_cast<chrono::microseconds>(elapsed).count();
    while( microseconds<asMS){
        elapsed = chrono::high_resolution_clock::now() - start;
        microseconds = chrono::duration_cast<chrono::microseconds>(elapsed).count();
    }
}

string asString(int i){
    // get time in seconds as formatted string
    // format: YYYYMMMDD-HH:mm:SS -- eg. 2020Feb06-22:08:15

    return "hello there";
}

int main(){
    printf("Info on Time library:\n");
    printf("=========================\n");
    time_t timer;
    printf("seconds since epoch: %i\n", time(&timer) );
    printf("seconds since epoch: %i\n", time(NULL) ); // same as previous

    //no official "sleep" function, and not usually advised to use anyway
    int t0=time(NULL);
    sleep(1);
    printf("time elapsed: %i\n",time(NULL)-t0);

    tm* curr_tm;
    time(&timer);
    curr_tm = localtime(&timer);
    char date_string[100];
    strftime(date_string, 50, "%Y%b%d-%H%M%S\n",curr_tm);
    printf("current datetime: %s\n", date_string);


    time_t rawtime;
    struct tm * timeinfo;
    time (&rawtime);
    timeinfo = localtime( &rawtime);
    cout << "year-month-day-weekday-hour-minute-second: ";
    cout << timeinfo->tm_year+1900 << "-"; // life starts in 1900
    cout << timeinfo->tm_mon+1 << "-"; // 0-indexed
    cout << timeinfo->tm_mday << "-";
    cout << timeinfo->tm_wday << "-";
    cout << timeinfo->tm_hour << "-";
    cout << timeinfo->tm_min << "-";
    cout << timeinfo->tm_sec << endl;

    auto start = chrono::high_resolution_clock::now();
    sleep(1);
    auto elapsed = chrono::high_resolution_clock::now() - start;
    long long microseconds = chrono::duration_cast<chrono::microseconds>(elapsed).count();
    cout << "elapsed in ms:" << microseconds << endl;
    cout << "in seconds: " << (float)microseconds/1e6 << endl;

    start = chrono::high_resolution_clock::now();
    sleep2(1.2);
    elapsed = chrono::high_resolution_clock::now() - start;
    microseconds = chrono::duration_cast<chrono::microseconds>(elapsed).count();
    cout << "2nd elapsed in ms:" << microseconds << endl;
    cout << "2nd in seconds: " << (float)microseconds/1e6 << endl;


    return 0;
}
