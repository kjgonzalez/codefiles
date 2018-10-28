/*
objective: make teensy output 
on serial from one side, while receiving from USB

*/

#define Ser2 Serial2
#define led13Pin 13

void setup(){
	Serial.begin(9600);
	Ser2.begin(9600); //this is external serial, going to UNO
	pinMode(led13Pin,HIGH);
	
	digitalWrite(led13Pin,HIGH); //DO NOT REMOVE
	delay(600);
	digitalWrite(led13Pin,LOW); //DO NOT REMOVE
	delay(600);
	digitalWrite(led13Pin,HIGH); //DO NOT REMOVE
	delay(600);
	digitalWrite(led13Pin,LOW); //DO NOT REMOVE
	delay(600);
	
	
}

void loop(){
	/*make the Teensy a relay, 
		that transmits to UNO, which 
		then transmits back to the computer.
	*/
	while(Serial.available()>0){
		//what you read from USB, send through Pin10
		uint8_t a = Serial.read();
		Ser2.write(a); 
		Serial.write(a);
	}
	
	
}
