/*
code objective: 
read in position of potentiometer, translate that to servo position.

option 1: follow square wave
option 2: use potentiometer to control servo
option 3: manually type in angle position
*/
#include <Servo.h>

Servo motor;


int setting=3; //whether manual or auto control
//1 - square wave
//2 - potentiometer
//3 - serial input
//4 - con't pot

int knobLoc=0; //pinlocation
int SampleRate=100; //ms
int value=0;
int incval=5;

void setup(){
delay(5000);
Serial.begin(9600);
motor.attach(3);
motor.write(115); //only if using con't rotation servo
Serial.println("115 is center");
//motor physical initialization

delay(1000);

}

void loop(){


// SETTING 1 - SQUARE WAVE //////////////////////////////////
  if(setting==1){
	value+=incval;
	motor.write(value);
	Serial.println(value);
	if(value>=179){
		value=0;
		motor.write(value);
		delay(1000);}
	delay(SampleRate);
	
	
  }//automatic movement
  
  
  
// SETTING 2 - POTENTIOMETER //////////////////////////////////
  else if(setting==2){
	  value=analogRead(knobLoc);
	  Serial.print(value);
	  delay(SampleRate);
	  value=map(value,0,1023,0,180);
	  value=constrain(value,0,180);
  
	  //analogWrite(3,value);
	  motor.write(value);
	  Serial.print(" : ");
	  Serial.println(value);
	  delay(100);
  }//manual control
  

  
  
  
  
// SETTING 3 - SERIAL INPUT //////////////////////////////////
  else if(setting==3){
	 
	  while(Serial.available()>0){
		  float command=Serial.parseFloat();
		  //command=constrain(command,0,180);
		 // command=map(command,0,180,600,2300);
		  Serial.print("sending ");
		  Serial.println(command);
		  
		  motor.writeMicroseconds(command);
		  delay(50);
		  }//do stuff if user inputs
	  
  }//serial input
  
  // SETTING 4 - con't pot ///////////////////////////////////
  else if(setting==4){
	  Serial.println(analogRead(0));
	  delay(100);
	  
  } //setting 4
  
  else{
	  Serial.println("error");
	  delay(1000);
	  
  }
  
  
  
  
  
} //end of loop
