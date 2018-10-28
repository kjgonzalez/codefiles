/*
main objective: correctly setup 
with pull-down (high true) button 
a "go" button. 

FOLLOW UP: works just fine
*/

int go=0;
int on=0;


void setup(){
  pinMode(12,INPUT); //take in button pulse (high-true)
  pinMode(8,OUTPUT); //light up LED ("motors")
  digitalWrite(8,LOW);
  pinMode(13,OUTPUT); //status LED
  digitalWrite(13,LOW);

  while(go==0){
    delay(500);
	digitalWrite(13,HIGH);
	delay(500);
	digitalWrite(13,LOW);
	go=digitalRead(12);	
  }//awaiting "go" input


  int length=5;//seconds to have "warning blink"
  int blink=100; //blink cycle half length (ms)
  for (int i=0;i<length*500/blink;i++){ 
	//will blink at 1cyc/(2*x) ms, for y seconds
	digitalWrite(13,LOW);
	delay(blink);
	digitalWrite(13,HIGH);
	delay(blink);
  }//warning loop



}//setup

void loop(){

	digitalWrite(8,HIGH);
	delay(400);
	digitalWrite(8,LOW);
	delay(100);

}//loop
