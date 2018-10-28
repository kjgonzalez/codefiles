/*
Objective: robot code. eventually will
run independent of computer. 

main command: wait 4 seconds, rotate in a circle.

*/

#include <Servo.h>
Servo mL; 
Servo mR; 




// System Variables
float WheelDiam=65; //mm
float Spacing=152; //mm
int ZeroPoint=1710; //"degrees" or "ms"

int button=0;

int rotateDelay=1190;
int moveDelay=1000;

void setup(){
	Serial.begin(9600);
	delay(5000);
	pinMode(12,INPUT);
	pinMode(13,OUTPUT);
	digitalWrite(13,LOW);
	
	Serial.println("starting...");
	
	mR.attach(3);
	mR.write(ZeroPoint);
	mL.attach(6);
	mL.write(ZeroPoint);
	
	//want to truly zero out the zero point
	
	while(digitalRead(12)==HIGH){
		ZeroPoint=constrain(map(analogRead(0),0,1023,1650,1750),1650,1750);
		mL.write(ZeroPoint);
		mR.write(ZeroPoint);
		Serial.println(ZeroPoint);
		delay(10);
	}
	blink();
	Serial.print("configured to ");
	Serial.println(ZeroPoint);
	
	
	
	
	delay(3000);
	MoveTo(30);
	
	
	
} //setup

void loop(){
	
	if(digitalRead(12)==LOW){
		blink();
		delay(3000);
		int dist=200;
		MoveTo(dist);delay(20);
		RotateTo(90);delay(20);
		MoveTo(dist);delay(20);
		RotateTo(90);delay(20);
		MoveTo(dist);delay(20);
		RotateTo(90);delay(20);
		MoveTo(dist);delay(20);
		RotateTo(90);delay(20);		
	}
	
	

	while(Serial.available()>0){
	int a=Serial.parseInt();
	float b=Serial.parseFloat();
	if(a==1){
		//rotate
		Serial.print("rotating ");
		Serial.print(b);
		Serial.println(" degrees");
		RotateTo(b);
	}
	
	
	else if(a==2){
		//translate
		Serial.print("moving ");
		Serial.print(b);
		Serial.println(" mm");
		MoveTo(b);	
	}
	
	
	else if(a==3){
		Serial.print("Setting ZP to ");
		Serial.println(int(b));
		ZeroPoint=int(b);
		mL.write(ZeroPoint);
		mR.write(ZeroPoint);
	}
	
	else if(a==4){
		Serial.print("Current ZP is ");
		Serial.println(ZeroPoint);
	}
	else Serial.println("error");
		
	}//command loop

delay(10);
}//main loop


void RotateTo(float inputAngle){
	// n1*A=n2*B. if u wanna rotate n1=360, 
	// wheels gotta rotate n2=n1*A/B degrees
	float WheelAngle=inputAngle*Spacing/WheelDiam;
	
	//stop possible movement
	mL.write(ZeroPoint);
	mR.write(ZeroPoint);
	delay(100);
	
	//for x ms, rotate in this direction
	mL.write(90+70*posneg(WheelAngle));
	mR.write(90+70*posneg(WheelAngle));
	for(int i=0;i<abs(WheelAngle)/360*1000;i++) delayMicroseconds(rotateDelay);
	//stop moving
	mL.write(ZeroPoint);
	mR.write(ZeroPoint);	
}


void MoveTo(float distance){
	//take in wheel diam and desired distance, get angle to move.
	
	//take in relative angle position
	// command, then move to that spot
	
	float angle=distance*2/WheelDiam*180/3.14159;
	angle=int(angle);
	
	//stop possible movement
	mL.write(ZeroPoint);
	mR.write(ZeroPoint);
	delay(100);
	
	//for x ms, rotate in this direction
	mL.write(90+70*posneg(angle));
	mR.write(90-70*posneg(angle));
	for(int i=0;i<abs(angle)/360*1000;i++) delayMicroseconds(1050);
	//stop moving
	mL.write(ZeroPoint);
	mR.write(ZeroPoint);
}


void tab(){
	Serial.print("\t");	
}

int posneg(float var){
	if(var<0) return -1;
	else if(var>0) return 1;
	else return 0;
}


void blink(){
	digitalWrite(13,HIGH);
	delay(50);
	digitalWrite(13,LOW);
	delay(50);
	digitalWrite(13,HIGH);
	delay(50);
	digitalWrite(13,LOW);
}
