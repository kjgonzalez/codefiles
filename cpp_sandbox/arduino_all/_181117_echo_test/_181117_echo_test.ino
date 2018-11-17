/*
Author: Kris Gonzalez
Created: 181117
Objective: Use a serial connection between pc-arduino to ensure that serial
  connection is functioning properly. this is a debugging program to be used
  in conjunction with related python script.

General Steps:
1. connect teensy
2. ensure "echo_test" is running on board
3. run python script of echo_test (e.g. "python3 echo_test_pc.py")
4. write in short text and send
5. board echoes same text back, and blinks LED
6. to quit, type 'q' and hit ENTER
How to Connect:
PC-usbcable-teensy/arduino

Example:
PC: one
BOARD: one
PC: two
BOARD: two
PC: lalalala
BOARD: lalalala
PC: q


*/

void setup(){
  Serial.begin(9600); // slow but easy to remember
  pinMode(13,OUTPUT); // additional indication that message was received
  Serial.println("starting");
  Serial.setTimeout(10);
  delay(1000);

}//setup

void loop(){
  while(Serial.available()>0){
    digitalWrite(13,HIGH);
    delay(300);
    digitalWrite(13,LOW);

    Serial.print("BOARD: ");
    Serial.println(Serial.readString());
  }//while data available
}//loop



// eof
