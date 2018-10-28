/*
code objective: 
 print out amount of time that has elapsed since
 program started running, and pause output when holding down a button
*/
//switch off, 5V in; switch on, pull to ground

//global var space
int button = 12; //button to pause displaying counter
int state=HIGH;


//setup
void setup() {
Serial.begin(9600);


}//setup




void loop(){
//first, read in value of button
state=digitalRead(button);

//next, do something about it.
  if(state==HIGH){
    Serial.println(millis());
	delay(1000);
  }//if pressed
  
  else if(state == LOW){
	Serial.print("button pressed");
	Serial.println("   i like tomatoes");
	delay(1000);
  } //else-if not pressed



}//loop


