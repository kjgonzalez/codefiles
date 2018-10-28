/*
main objective: learn how to send a serial
command to arduino from serial monitor.
should be able to write something like "1"
and have the LED blink once.

UDPATE: it works. 
*/

int n=0;


void setup()
{

	Serial.begin(9600);
	pinMode(12,OUTPUT);
	delay(5000);
	Serial.println("starting. lol ..");


}

void loop(){

	while(Serial.available()>0){
		n=Serial.parseInt();
		Serial.println(n);

			n=constrain(n,1,10);
			
			for(int i=0;i<n;i++){
				digitalWrite(12,HIGH);
				Serial.println("high");
				delay(300);
				digitalWrite(12,LOW);
				Serial.println("low");
				delay(300);
			} //blink forloop
	}//whileloop
	delay(100);
	//Serial.print("ready \t");
}
