/*
objective: understand how arrays and 
pointers work. essentially, this is 
a refresher on C++. 

*/

int loopTime=0;
int prevTime=0;
int avg=0;

int prevBTN=0;
int currBTN=0;


void setup(){
delay(5000);
Serial.begin(9600);
Serial.println("Starting...");
pinMode(12,INPUT);
prevBTN=0;

}//setup

void loop(){

{
currBTN=digitalRead(12);	
}






}//main loop



void tab(){
	Serial.print("\t");
}