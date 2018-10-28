/*
Main Objective: will calibrate a servo motor and 
find out what each motor "write" command 
corresponds to in terms of RPM. for example, if 
"115" is zero, want to know what "110" command 
will output, and in which direction (CCW,CW from
above looking down). 
*/

#include <Servo.h>
Servo motor;

int SampleSize=2;
int BaseDelay=10;
int ArmNumber=5;


int smin=1023;
int smax=0;
int smid=0;
int sval=0;
int prevSNS=0;
int currSNS=0;
int countSNS=0;
float hz=0;
float currLatch=0;
float prevLatch=0;


void setup(){
	Serial.begin(9600);
	delay(3000);
	Serial.println("motor center: 114"); 
	motor.attach(3);
	motor.write(114);
	Serial.println("starting...");
		
	
	//calibrate smin and smax, via rotating the arm once
	motor.write(80);
	int n;
	//for 4 seconds, take in values and record which 
	for(int i=0;i<3000;i++){
		delay(1);
		sval=analogRead(0);
		if(sval>smax) smax=sval;
		else if(sval<smin) smin=sval;
	}
	smid=(smax+smin)/2;
	motor.write(114);
	
	Serial.println("measured values");
	Serial.print(smin); tab();
	Serial.print(smid); tab();
	Serial.print(smax); tab();
	Serial.println("");
	
	//initialization
	prevLatch=millis();
	
	delay(5000);
}//setup

void loop(){
	delay(BaseDelay);
	sval=analogRead(0);
	//eventually comment out
//	Serial.println(sval);
	
	while(Serial.available()>0){
		//create input option
		float command= Serial.parseFloat();
		
		if(command<0){
		command=command*(-1);
		command=constrain(command,1,10);
		SampleSize=command;
		countSNS=0;	
		}//change sample rate
			
		else {
			command=constrain(command,0,180);
			motor.write(command);
			Serial.print("Sending ");
			Serial.println(command);
		}//change motor command
		
		
		
	} //command loop
	
	
	// LATCH HELP
	currSNS=eitheror(sval,smid);
	if(prevSNS==0 && currSNS==1){
		currLatch=millis();
		//Serial.println(millis());
		
		
		countSNS++;
		prevSNS=currSNS;
	}
	else {}//latchSNS=0;
	prevSNS=currSNS;
	
	// time to calculate period, hertz
	if(countSNS==SampleSize*ArmNumber){
		countSNS=0;
		hz=1000*SampleSize/(currLatch-prevLatch);
		float per=(currLatch-prevLatch)/(SampleSize);
		
		prevLatch=currLatch;
		Serial.print("Hz (");
		Serial.print(SampleSize);
		Serial.print("):");
		tab();
		Serial.print(hz);
		tab();
		Serial.print(per);
		Serial.println("");
	}
	
	
}//main loop


void tab(){
	Serial.print("\t");
}


int eitheror(int var,int threshold){
	if(var>threshold)return 1;
	else return 0;
}