/*
will try to run 2 servos off of specific wiring config: 9v and 6v 
source in parallel, the 9v connecting to arduino and 6v connecting 
to both motors in parallel, then signals going from arduino to 
both motors.

FOLLOW UP: IT WORKED. no shorts, no resets. note: motors sping in 
opp. directions.

*/

#include <Servo.h>

Servo m1;
Servo m2;

void setup(){

//pre-start warning
pinMode(13,OUTPUT);
for(int i=0;i<6;i++){
	delay(500);
	digitalWrite(13,HIGH);
	delay(500);
	digitalWrite(13,LOW);
}//start warning loop

Serial.begin(9600);
m1.attach(3);
m2.attach(6);
m1.write(0);
m2.write(0);



for(int i=0;i<21;i++){
//cycle m1:
	delay(1000);
	m1.write(180);
	delay(500);
	m2.write(180);
	delay(500);
	m1.write(0);
	delay(500);
	m2.write(0);
}//motor loop

}//setup


void loop(){
} // loop