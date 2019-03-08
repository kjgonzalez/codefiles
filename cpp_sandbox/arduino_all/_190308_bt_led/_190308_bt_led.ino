/*
Author: Kris Gonzalez
Objective: control led via bluetooth.
ASSUMPTIONS:
    * python script only runs on Windows
    * MUST use python3 on pc(otherwise have bytes/str type issue)

General steps: 
1. run python script, send [w,a,s,d] over BT (bytes)
2. bt receives, sends comm to teensy, teensy changes led state
3. print received key to pc serial monitor

note about command / action:
CMD |int | action
w   |119 | 'fwd', 1
a   |97  | 'bwd', 0
s   |115 | 'lhs', 0
d   |100 | 'rhs', 1
*/

int led = 13; // set led pin

void setLED(int des){
    /* set desired led state. make sure invalid values are ignored. */
    if(des == 0 || des == 1) digitalWrite(led,des);
}//void setLED

void setup() {
    pinMode(led,1); // 1 = OUTPUT
	Serial.begin(38400); // pc / usb serial (give status)
	Serial1.begin(38400); // hardware serial (to bluetooth)
	delay(2000);
	Serial.println("Hello World START");

}//setup

void loop() {
	int inByte; // will interpret byte value of letter (see ascii table)
	if(Serial1.available()>0){
        inByte=Serial1.read();
        if(inByte=='w'){
            Serial.println("fwd");
            setLED(1);
        } 
        else if(inByte=='a'){
            Serial.println("cd lhs");
            setLED(0);
        }
        else if(inByte=='s'){
            Serial.println("bwd");
            setLED(0);
        }
        else if(inByte=='d'){
            Serial.println("rhs");
            setLED(1);
        }
	}//if bt data avail
}//loop