/*
objective: use transistor to light up LED on command.
will send controlled signal to transistor, will activate, 
and thus the LED will either be turned on or off via the 
transistor being activated.
note: PNP 
*/

int onflag=0;


void setup(){
pinMode(3,OUTPUT);

Serial.begin(9600);
Serial.println("Device On");
delay(5000);

Serial.println("start...");


}

void loop(){
	delay(100);
	
	while(Serial.available()>0){
		int value2=Serial.parseInt();
		Serial.println(value2);
		analogWrite(3,value2);
		/*
		if(onflag==0){
			digitalWrite(3,HIGH);
			onflag=1;
			}//caseOFF
		else{
			digitalWrite(3,LOW);
			onflag=0;
			}//caseON
		*/
		
		
		
	}//userinput


}//loop 
