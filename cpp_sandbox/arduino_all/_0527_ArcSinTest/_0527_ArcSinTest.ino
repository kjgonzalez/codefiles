/*
main objective: verify that arduino 
can calculate the arc_blank of sine,
cosine, and tangent.

*/

#include <math.h>

#define pi 3.14159;

float rad2deg=180/pi;

void setup(){
Serial.begin(9600);
delay(5000);
Serial.println("starting...");




}

void loop(){

while(Serial.available()>0){
	float n=Serial.parseFloat();
	Serial.print(asin(n)*rad2deg); 
	Serial.print("\t");
	Serial.print(acos(n)*rad2deg); 
	Serial.print("\t");
	Serial.println(atan(n)*rad2deg); 
	
}
delay(10);
}
