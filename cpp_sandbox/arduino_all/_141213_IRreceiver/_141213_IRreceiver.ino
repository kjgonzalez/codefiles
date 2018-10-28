//objective: understand how IR receiver sends data. hopefully, will be like a resistor



#define IRin 2
#define LEDpin 5


void cap(){
//ISR for pin2
if(digitalRead(2)==LOW) {
	digitalWrite(LEDpin,HIGH);
	Serial.println("0");
}


else {
	digitalWrite(LEDpin,LOW);
	Serial.println("1");
}

}// ISR



void setup(){
	Serial.begin(56000);
	pinMode(LEDpin,1); //set as output
	digitalWrite(LEDpin,0); //initialize as off
	attachInterrupt(0,cap,CHANGE);
	Serial.println("starting...");
} //setup

void loop(){
// 	int sval=digitalRead(IRin);
// 	Serial.println(sval);
// 	millis(100);

	//wait, unless data comes through

// 	while(Serial.available()>0){
// 		int a=Serial.parseInt();
// 		if(a<0 || a>1) a=0;
// 		digitalWrite(LEDpin,a);
// 		Serial.print("value: ");
// 		Serial.println(a);
//	}//read in available serial data

}//main loop
