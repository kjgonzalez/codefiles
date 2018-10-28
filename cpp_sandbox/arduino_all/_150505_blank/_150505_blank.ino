//this code does nothing, allows arduino to sit inactive.

#define inPin 4
#define ledPin 13


void setup(){
	pinMode(ledPin,OUTPUT);
		
}//setup


void loop(){
	digitalWrite(ledPin,HIGH);
	delay(100);
	digitalWrite(ledPin,LOW);
	delay(100);
}//loop