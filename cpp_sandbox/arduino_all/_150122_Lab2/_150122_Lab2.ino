/*
objective: complete lab 2: read 
  from an IR sensor, and perform an
  action once a threshold has been crossed
*/


void setup(){
	Serial.begin(9600);
	pinMode(13,OUTPUT);
	digitalWrite(13,LOW);
	digitalWrite(13,HIGH);
	delay(200);
	digitalWrite(13,LOW);
	
	delay(1000);
	Serial.println("starting");
	
}

void loop(){
	int a = analogRead(0);
	Serial.println(analogRead(0));
	if(a>300) digitalWrite(13,LOW);
	else digitalWrite(13,HIGH);
	delay(200);	
}