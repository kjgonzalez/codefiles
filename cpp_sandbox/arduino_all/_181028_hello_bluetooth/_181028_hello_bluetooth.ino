/*
Author: Kris Gonzalez
Date Created: 181028
Objective: initial setup of bluetooth on arduino teensy.
Board:


KJGNOTE: ALL THE ABOVE CODE IS OUT OF DATE, AND WILL BE UPDATED

*/



#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
myservo.attach(9);  // attaches the servo on pin 9 to the servo object
Serial.begin(9600);
Serial.println("serial port open");

}

void loop() {
	int comvalue = 0;
	if(Serial.available() > 0) {
		comvalue = Serial.parseInt();
		Serial.print("received (microseconds): ");
		Serial.println(comvalue);
		myservo.writeMicroseconds(comvalue);
	} //if new value received

}//mainloop
