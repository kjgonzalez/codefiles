/*
main objective: be able to serially input a number / combo, 
and be able to control different parameters of micro-p. 

example: either rotate servo or change LED blink rate

UDPATE: success

*/

#include <Servo.h>
Servo motor;




void setup(){
Serial.begin(9600);
delay(3000);
Serial.println("Starting...");

pinMode(13,OUTPUT);
motor.attach(3);
motor.write(114);


} //setup

void loop(){

while(Serial.available()>0){
	int a=Serial.parseInt();
	int b=Serial.parseInt();
	if(a==1){
		if(b==0) b=LOW;
		else b=HIGH;
		Serial.print("Changing to ");
		Serial.println(b);
		digitalWrite(13,b);
		
	}// a=1
	else {
		b=constrain(b,0,180);
		Serial.print("Sending ");
		Serial.println(b);
		motor.write(b);
	}// other cases
}//while have serial input

delay(10);
}//main loop