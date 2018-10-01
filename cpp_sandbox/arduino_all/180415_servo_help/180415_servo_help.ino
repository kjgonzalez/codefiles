/*
Author: Kris Gonzalez
Date Created: 180415
Objective: help figure out why another microcontroller having 
	issues driving a servo.

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
