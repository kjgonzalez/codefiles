/*
Objective: be able to tell the wheel to rotate to a 
specific position as well as to rotate at a particular
velocity. 
*/
#include <Servo.h>
Servo motor;

int wheelDiam=65; //mm
int zeroPoint=114; //degrees (for servo library)


int start=1;


//position command: 1 
//velocity command: 2

void setup(){
	Serial.begin(9600);
	delay(5000);
	Serial.println("starting...");
	
	motor.attach(3);
	motor.write(114);
	
	
	
} //setup

void loop(){

	while(Serial.available()>0){
			int option=Serial.parseInt();
			float val=Serial.parseFloat();
			
			if(option==1){ //position command
				//take in relative angle position 
				// command, then move to that spot
				
				//stop possible movement
				motor.write(zeroPoint);
				Serial.print("going to ");
				Serial.println(val);
				delay(500);
				
				//for x ms, rotate in this direction
				motor.write(90+60*posneg(val));
				for(int i=0;i<abs(val)/360*1000;i++) delayMicroseconds(1021);
				
				//stop moving
				motor.write(zeroPoint);
				
			}//option 1 - position
			

			
			else if(option==2) { //velocity command
				
				// velocity command given in hertz
				val=velTranslate(val);
				//motor command translated to absolute "angle"
				motor.write(val);
				Serial.print("sending ");
				Serial.println(val);
				
			}//option 2 - velocity command
			
		}//take in command
delay(50);

}//main loop


int velTranslate(float hz){
	//  take in desired velocity (Hz) and 
	//  translate to motor.write command
	
	//get sign of value
	
	float posneg=0;
	if(hz<0)posneg=-1;
	else if(hz>0)posneg=1;
	else return zeroPoint;
	
	//get magnitude of value
	hz=abs(hz);
	hz=constrain(hz,0,1.1);
	float a=35;
	float b=-1.7;
	float c=0.9;
	
	//turn into relative motor command
	hz=pow((1/hz-c)/a,1/b);	
	hz=hz*posneg;
	
	
	//turn into absolute motor command (between 0,180, w/ zeropoint)
	
	return constrain(hz+zeroPoint,0,180);
	
	//update: this guy WORKS just fine.
} 


int posneg(float var){
	if(var<0) return -1;
	else if(var>0) return 1;
	else return 0;	
}