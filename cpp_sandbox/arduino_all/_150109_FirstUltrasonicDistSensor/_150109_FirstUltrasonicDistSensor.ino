/*
objective: first test in using ultrasonic range finder
main idea: will use "pulsein(...)" function to help
  understand how range finder works, plus making simple
  copy-and-paste code for other projects
  
  UPDATE: code works reliably, sensor has a range of about 1-80in (3-200cm).
  code below has been changed from what was found online, note that data sheet 
  asks for a 10us trigger, but 100us trigger has been more reliable, i.e. provides
  less out-of-range errors (returning zero while within range).
  
*/


#define trigPin 7
#define echoPin 8


uint16_t getMiddle(){
	digitalWrite(trigPin, HIGH);
	delayMicroseconds(100);
	digitalWrite(trigPin, LOW);
	
	uint16_t dist_cm = pulseIn(echoPin, HIGH); //time to return in microseconds
	return dist_cm*.0172; //.0172 = 343 cm/us * 1/2

}


void setup() {
	Serial.begin (9600);
	pinMode(trigPin, OUTPUT);
	pinMode(echoPin, INPUT);
}

void loop() {
	
// 	digitalWrite(trigPin, HIGH);
// 	delayMicroseconds(100);
// 	digitalWrite(trigPin, LOW);
// 	
// 	int dist_cm = pulseIn(echoPin, HIGH); //time to return in microseconds
// 	dist_cm = dist_cm*.0172; //.0172 = 343 cm/us * 1/2
	Serial.println(getMiddle());
	delay(800);
}
