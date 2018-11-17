/*
Author: Kris Gonzalez
Create Date: 2017-Nov-02
Objective: first-time communication with bluetooth, need
	to come up with way to talk to HC05 via teensy. will use
	PC-Serial-Teensy-Serial1-Bluetooth communication.
	General scheme: 
	1. use serial monitor to send data to teensy
	2. teensy bounces same information to bluetooth
	3. whenever bluetooth returns info, bounce info to serial
		monitor

*/

//String str ="test";

void setup() {
	Serial.begin(38400); // pc / usb serial
	Serial1.begin(38400); // hardware serial (to bluetooth)
	delay(2000);
	Serial.println("Hello World");
	delay(2000);
	Serial.println("Hello World START");
	// Serial.println(str);

}//setup

void loop() {
	int inByte;
	String ins="";
	if(Serial.available()>0){
		//inByte = Serial.read();
		ins = Serial.readString();
		Serial.print("PC: ");
		//Serial.write(inByte);
		//Serial1.write(inByte);
		Serial.print(ins); //monitor alrdy sending NL + CR
		Serial1.print(ins);
	}//if pc data available
	
	if(Serial1.available()>0){
		// Serial.print("BT: ");
		// while(Serial1.available()>0){
			// inByte=Serial1.read();
			// Serial.write(inByte);
		// }//while-available
		
		// //quick, debugging
		Serial.write(Serial1.read());
		
		// //slow, debugging
		// ins = Serial1.readString();
		// Serial.print("BT: ");
		// Serial.print(ins);
	}//if bt data avail

}//loop