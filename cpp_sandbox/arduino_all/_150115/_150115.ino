/*
objective: make an LED blink when a switch is pressed. 
	LED is active high, switch is closed-high
*/

#define ipin 3
#define opin 5

void setup(){
pinMode(ipin,INPUT);
pinMode(opin,OUTPUT);
}

void loop(){
int a=digitalRead(ipin);
if(a==HIGH) digitalWrite(opin,HIGH);
else digitalWrite(opin,LOW);


}
