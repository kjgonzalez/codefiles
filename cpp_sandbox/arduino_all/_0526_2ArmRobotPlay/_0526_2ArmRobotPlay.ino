/*
main objective: use two potentiometers to control the 
movement of a 2 link vertical arm robot. 

*/

#include <Servo.h>
Servo m1;
Servo m2;

//blue pot, A0, to large servo, D3
//black pot, A1, to small servo, D6

//m1 limits
int m1min=15;
int m1max=155;
//m2 limits
int m2min=4;
int m2max=180;




void setup(){
	delay(4000);
	Serial.begin(9600);
	Serial.println("Starting");
	m1.attach(3); //large servo motor
	m2.attach(6); //small servo motor
	
	m1.write(m1Read());
	m2.write(m2Read());
	
	
notep
} //setup

void loop(){
	int ang1=m1Read();
	int ang2=m2Read();
	

	Serial.print(ang1);
	Serial.print("\t");
	Serial.println(ang2);
	
	m1.write(ang1);
	m2.write(ang2);

	delay(30);
	
} //main loop


int m1Read(){
	return constrain(map(analogRead(0),0,1023,m1min,m1max),m1min,m1max);
}

int m2Read(){
	return constrain(map(analogRead(1),0,1023,m2min,m2max),m2min,m2max);
}
