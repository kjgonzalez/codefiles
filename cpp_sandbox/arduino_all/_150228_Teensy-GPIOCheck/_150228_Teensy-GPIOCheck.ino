/*
objective: GPIO check
	things that must be tested 
	to ensure quality capability
	on the Teensy 3.1:
	GPIO IO - done
	ADC - done
	PWM - done
	interrupts - done
	Serial - done (USB only)
*/

#define ledCheckPin 3
#define led13Pin 13
#define buttonPin 0


void pressed(){
	//run this when button is pressed.
	if(digitalRead(buttonPin)==HIGH) digitalWrite(ledCheckPin,HIGH);
	else digitalWrite(ledCheckPin,LOW);
}


void setup(){
pinMode(led13Pin,OUTPUT); // DO NOT REMOVE
pinMode(ledCheckPin,OUTPUT);

pinMode(buttonPin,INPUT);
attachInterrupt(buttonPin,pressed, CHANGE);
Serial.begin(9600);


} //setup

void loop(){
digitalWrite(led13Pin,HIGH); //DO NOT REMOVE
delay(1000);

// int i=0;
// while(i<80){
// 	uint8_t a = digitalRead(buttonPin);
// 	if(a==HIGH) digitalWrite(ledCheckPin,HIGH);
// 	else digitalWrite(ledCheckPin,LOW);
// 	
// 	//DO NOT REMOVE
// 	delay(100);
// 	i++;
// }//while loop


digitalWrite(led13Pin,LOW); //DO NOT REMOVE
delay(1000);
Serial.println("printme");
} //loop
