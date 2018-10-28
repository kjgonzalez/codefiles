/*
Kristian Gonzalez
11/15/2014
main objective: 
	take in a potentiometer reading, translate to (x,y)
	coordinates, then send command to 2 servos.
	will feature a start/pause/play button soon
	
README: current ability
* have potentiometer move a desired (x,y) position
* control two servos in joint space
* upgraded baud rate to 19200, using #define more
* using pwm millisecond control, not angle control on servos
	
	
*/

#include <Servo.h>
Servo m1;
Servo m2;

//blue pot, A0, to large servo, D3
//black pot, A1, to small servo, D6

// physical properties (verified 1121'14)
#define r1 5
#define r2 2.8750
#define pi 3.14159
#define baudRate 19200
#define m1Pin 3
#define m2Pin 6

// min/max degree lims (ver 1121'14), matlab
#define m1minDEG 6
#define m1maxDEG 110
#define m2minDEG 16
#define m2maxDEG 173

// MUST VERIFY VALUES
#define m1minPWM 650
#define m1maxPWM 1550
#define m2minPWM 638
#define m2maxPWM 2300


//persistent (x,y) coord setup (ver 1121'14)
float x=3;
float y=3;
#define xlimL 0 //inch
#define xlimH 7.8 //inch
#define ylimL 0 //inch
#define ylimH 7.8 //inch
#define incr .1 //inch

//temporary: for tuning
int aa=600;
int bb=2300;



int m1Read(){//delme
	//return m1 angle (deg) directly from pot reading, A0
	return constrain(map(analogRead(0),0,1023,m1minDEG,m1maxDEG),m1minDEG,m1maxDEG);
}
int m2Read(){//delme
	//return m2 angle (deg) directly from pot reading, A1
	return constrain(map(analogRead(1),0,1023,m2minDEG,m2maxDEG),m2minDEG,m2maxDEG);
}

int m1MilliRead(){//delme
	return map(analogRead(0),0,1023,650,1550);
}
int m2MilliRead(){
	return map(analogRead(1),0,1023,0,2700); //???
}

//return required motor angles (VERIFY!)
float getAngle1_DEG(float xd, float yd){
	/*from matlab: 
	R = sqrt(xd^2+yd^2);
	phi = acos(xd/R);
	beta=acos((r1^2+R^2-r2^2)/(2*R*r1));
	gamma=acos((r2^2+R^2-r1^2)/(2*R*r2));
	a1=phi+beta; %CHANGE HERE FOR ELBOW CONFIG (+=up)
	a2=beta+gamma;*/
	float R = pow(	xd*xd+yd*yd	,.5);
	float phi = acos(xd/R);
	
	float beta=acos(	(r1*r1+R*R-r2*r2 ) / (2*R*r1)	);
	// float gamma=acos(	(r2*r2+R*R-r1*r1) / (2*R*r2)	); //necessary for a2
	return (phi+beta)*180.00/pi; // CHANGE HERE FOR ELBOW CONFIG (+=up)
} //angle 1
float getAngle2_DEG(float xd, float yd){
/*from matlab: 
R = sqrt(xd^2+yd^2);
phi = acos(xd/R);
beta=acos((r1^2+R^2-r2^2)/(2*R*r1));
gamma=acos((r2^2+R^2-r1^2)/(2*R*r2));
a1=phi+beta; %CHANGE HERE FOR ELBOW CONFIG (+=up)
a2=beta+gamma;*/
	float R = pow(	xd*xd+yd*yd	,.5);
	//float phi = acos(xd/R); //necessary for a1
	float beta=acos(	(r1*r1+R*R-r2*r2 ) / (2*R*r1)	);
	float gamma=acos(	(r2*r2+R*R-r1*r1) / (2*R*r2)	); //necessary for a2
	return (beta+gamma)*180/pi; // CHANGE HERE FOR ELBOW CONFIG (+=up)
}//float getAngle2_DEG

int Deg2PWM(float angleDEG, int minval, int maxval){
//give this specific output to the motor function "motor.write()"
	return map(angleDEG,0,180,minval, maxval);
}//int Deg2PWM


int mapFloat(float var1,float xmin,float xmax, float ymin, float ymax){
	//float type version of map() function. 
	// takes IN float types, STILL returns int type
	var1 = (ymax-ymin)/(xmax-xmin)*var1+(ymin-(ymax-ymin)/(xmax-xmin)*xmin);
	int var2= (int) var1;
	return var2;
}

float pyt(float var1, float var2){
	return pow(var1*var1+var2*var2,.5);
}

void getNewXY(){
	//in bit10 range
	int xtemp=analogRead(1);
	int ytemp=analogRead(0);
	ytemp=1023-ytemp;
	
	//move cursor with enough input, and	\
	prevent desired location from		\
	being outside the allowable area.
	float R=0;
	if(xtemp-500>100){
		//desire to move x+
		R=pyt(x+incr,y);
		if(R<r1+r2)	x=constrain(x+incr,xlimL,xlimH);
		}
	else if(xtemp-500<-100){
		//desire to move x-
		R=pyt(x-incr,y);
		if(R>r1-r2) x=constrain(x-incr,xlimL,xlimH);
		}
		
	if(ytemp-500>100){
		//desire to move y+
		R=pyt(x,y+incr);
		if(R<r1+r2) y=constrain(y+incr,ylimL,ylimH);
	}
	else if(ytemp-500<-100){
		//desire to move y-
		R=pyt(x,y-incr);
		if(R>r1-r2) y=constrain(y-incr,ylimL,ylimH);
	}
}




void showXY(){
	Serial.print(x);
	Serial.print("\t");
	Serial.print(y);
}

int IN_SERIAL(){
	int a=0;
	while(Serial.available()>0){
		a = Serial.parseInt();
	}//whileloop
	return a;
}





void setup(){
// INTITIALIZATIONS HERE /////////////////////////////////////////////////
	delay(500);
	Serial.begin(baudRate);
	Serial.println("Starting");
	m1.attach(m1Pin); //large servo motor
	m2.attach(m2Pin); //small servo motor

	
} //setup

void loop(){

// READ IN DESIRED POSITION	//////////////////////////////////////////////
	getNewXY();
	
// PRINT WHERE CURSOR IS /////////////////////////////////////////////////
	//for user help, print out current (xd,yd)
	showXY();
	Serial.print("\t");
	//more to print below

// CONVERT TO A1,A2 //////////////////////////////////////////////////////
	
	int a1=getAngle1_DEG(x,y);
	int a2=getAngle2_DEG(x,y);	
 	Serial.print(a1);
 	Serial.print("\t");
 	Serial.print(a2);
 	Serial.print("\n");

// MOVE MOTOR ////////////////////////////////////////////////////////////	
	
	//	1. get desired location.	\
		2. convert to degrees		\
		3. convert to pwm			\
		4. send to motor

 	m1.write(a1);
 	m2.write(a2);
	


/*
//quick debug of m2


//Serial.println(map(analogRead(0),0,1023,0,90));
//m2.write(map(analogRead(0),500,1023,0,90));

	int var1=constrain(map(analogRead(1),500,1023,0,90),0,90);

	m2.write(var1);
	Serial.print(analogRead(1));
	Serial.print("\t");
	Serial.println(var1);
*/




// ENABLE attempt 1 FIRST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

	//attempt 1 - give angle value directly as motor command
//  	m1.write((int) m1Angle);
//  	m2.write((int) 180-m2Angle); //posibly needs change of ref: 180-m2Angle
	
	//attempt 2 - convert angle value to more precise ms command
// 	m1.writeMicroseconds(mapFloat(m1Angle,m1minDEG,m1maxDEG,m1minPWM,m1maxPWM));
// 	m2.writeMicroseconds(mapFloat(m2Angle,m2minDEG,m2maxDEG,m2minPWM,m2maxPWM)); //possibly needs ref change, map(180-m2Angle,...)
	
	// what just happened? here:	\
		1. take in m1Angle, between allowable min/max of particular Servo	\
		2. convert to pwm signal, between allowable min/max of Servo		\
		3. return as int, converted from float, to motor command as ms signal


// SHOW MOTOR COMM ///////////////////////////////////////////////////////
	//for user help, print out current (xd,yd)
// 	Serial.print(m1Angle);
// 	Serial.print("\t");
// 	Serial.println(m2Angle);
	//Serial.print("\t");
	
	
/*	
	int ang1=m1MilliRead();
	int ang2=m2MilliRead();
	
	
	Serial.print(ang1);
	Serial.print("\t");
	Serial.println(ang2);
	
	m1.write(ang1);
	m2.write(ang2);
*/

	delay(15); //slight delay to reduce jerkiness
	
} //main loop


