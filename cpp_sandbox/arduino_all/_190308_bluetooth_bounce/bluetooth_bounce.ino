/*
Author: Kris Gonzalez
Create Date: 2017-Nov-02
Objective: First-time communication with bluetooth, need to come up with way 
    to talk to HC05 via teensy. will use PC-Serial-Teensy-Serial1-Bluetooth 
    communication. general operation:
        1. use serial monitor to send data to teensy
        2. teensy bounces same information to bluetooth
        3. whenever bluetooth returns info, bounce info to serial monitor

ASSUMPTIONS:
    * example2 only runs on Windows
    * MUST use python3 on pc(otherwise have bytes/str type issue)
    * HAS BEEN PROVEN TO WORK (KJG190308)

SETUP STEPS: 
1. Using a breadboard or other, wire the teensy & HC05 as in "WIRING 
    REQUIREMENT"
2. Plug in the board (double check that you've wired correctly!)
3. Upload this ino file to board
4. If this is the first time your computer's connecting to the HC05, you will 
    need to actually pair the HC05. open bluetooth settings, click "add 
    bluetooth or other device", look for whatever name you've given it (e.g. 
    "KJGBT"), connect, enter in password (default: 1234), and you should be 
    paired.
5. Using python3, start python script. the screen should be ready for input, 
    and pressing "q" will end the script.

WIRING REQUIREMENT: 
TEENSY------|-HC05 bluetooth
SR1 (p0)    | TXD
ST1 (p1)    | RXD
3V3 (top-L) | VCC
GND (any)   | GND
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