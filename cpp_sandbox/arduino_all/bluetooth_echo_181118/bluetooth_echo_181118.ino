/*
Author: Kris Gonzalez
Created: 181118
Objective: Use a serial connection between pc-arduino to then send some text
  through bluetooth, which then transmits it somewhere else.

Ideal Connection:
pc-arduino-bluetooth-pc
note: pc is running 2 diff programs at once (2-way comm, and 1-way receive)

General Steps:
1. connect teensy
2. ensure "echo_test" is running on board
3. run python script of echo_test (e.g. "python3 echo_test_pc.py")
4. write in short text and send
5. board echoes same text back, and blinks LED
6. to quit, type 'q' and hit ENTER

How to Connect:
PC-usbcable-teensy/arduino-bluetooth

Example:

*/

void setup(){
  // possible bauds: 38400, 115200
  Serial.begin(38400);  // pc-arduino comm
  Serial1.begin(38400); // arduino-bluetooth comm
  pinMode(13,OUTPUT); // additional indication that message was received
  Serial.println("BOARD: Starting...");
  Serial.setTimeout(10);
  Serial1.setTimeout(10);
  delay(1000);

}//setup

void loop(){
  String inp="";
  digitalWrite(13,HIGH);
  delay(100);
  digitalWrite(13,LOW);
  delay(100);
  if(Serial.available()>0){
    inp=Serial.readString();
    Serial.print("BOARD: received: ");
    Serial.println(inp);
    Serial.print("BOARD: sending... ");
    Serial1.println(inp); //keep everything as bytes, just bounce over
    Serial.println("done.");

  //   Serial.print("BOARD: sending.");
  //   while(Serial.available()>0){
  //     Serial1.write(Serial.read()); //keep everything as bytes, just bounce over
  //   }//while data sending
  //   Serial.println(" done.");
  }//if data available
}//loop



// eof
