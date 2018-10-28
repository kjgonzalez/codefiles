//kjg first sketch:

int n=100;
int io=13;

void setup(){
	pinMode(io,OUTPUT);

}//SETUP

void loop() {

	digitalWrite(io,HIGH);
	delay(1500);
	digitalWrite(io,LOW);
	delay(n);
	digitalWrite(io,HIGH);
	delay(n);
	digitalWrite(io,LOW);
	delay(n);
	digitalWrite(io,HIGH);
	delay(n);
	digitalWrite(io,LOW);
	delay(n);
}//loop