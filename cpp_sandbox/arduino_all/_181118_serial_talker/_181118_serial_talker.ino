/*
Objective: just send a steady message out and listen for it on computer. this
  program only created to help python script.

python script objective: be able to connect to a given serial port and listen

general steps:
1. upload to board
2. let board run
3. run python script that listens and publishes incoming serial stream
*/


void setup(){
  Serial.begin(115200); // slow but easy to remember
  pinMode(13,OUTPUT); // additional indication that message was received
  Serial.println("starting");
  Serial.setTimeout(10);
  delay(1000);

}//setup

int i=0;
void loop(){
  digitalWrite(13,HIGH);
  delay(300);
  digitalWrite(13,LOW);
  Serial.print("BOARD: hello, ");
  Serial.println(i++);
  delay(700);
}//loop



// eof
