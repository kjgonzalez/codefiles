/*
be sure to download zip of repo and install in arduino. 
repo: https://github.com/duff2013/Snooze

with this lib, you can get sub-1mA power consumption!!!
*/

#define led 13
#include <Snooze.h>
// SnoozeDigital digital;
// install drivers to a SnoozeBlock
SnoozeTimer timer;
Snoozelc5vBuffer lc5vBuffer;
SnoozeDigital digital;
SnoozeBlock config_teensyLC(lc5vBuffer,digital,timer);





void setup() {
pinMode(led, OUTPUT);
// timer.setTimer(5000); // enable this to turn on sleeping for a set amount of time
}

void loop() {
/********************************************************
feed the sleep function its wakeup parameters. Then go
to deepSleep.
********************************************************/
int who = Snooze.deepSleep( config_teensyLC );// return module that woke processor

digitalWrite(led, HIGH);
delay(5000);
digitalWrite(led, LOW);
}