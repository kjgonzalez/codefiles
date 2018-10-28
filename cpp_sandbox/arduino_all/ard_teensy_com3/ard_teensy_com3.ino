/*
please let this work :(
*/
#include <.ard_teensy_com3.vsarduino.h>
void setup(){
	Serial.begin(9600);
	delay(1000);
	Serial.println("starting");
}

void loop(){
	while(Serial.available()>0){
		Serial.println(Serial.parseInt());
	}
}
