/*
main objective: use serial input to move servo motor, 
collect data on different points from IR sensor
that is attached to top of servo
*/

#include <Servo.h>

Servo motor;

int points=4; //number of points to collect per side
int delayTime=100; //ms

void setup(){
	Serial.begin(9600);
	delay(5000); 
	Serial.println("Starting...");
	motor.attach(9);
	motor.write(90);
	
	
} //setup

void loop(){

	while(Serial.available()>0){
		
		//take in serial input
		int blah=Serial.parseInt();
		
		int count=2*points-1; //should be 7 if points=4
		
		float nextAngle=180;
		motor.write(nextAngle);
		delay(delayTime*2);
		
		float rL[points];
		float aL[points];
		float rR[points];
		float aR[points];
		
		for(int i=0;i<count;i++){
		Serial.println(irSensorCm(analogRead(0)));
			if(i<points-1){//left
				aL[i]=nextAngle;
				rL[i]=irSensorCm(analogRead(0));
				nextAngle-=180/(count-1);
				motor.write(nextAngle);
			}//left side
		
			else if(i==points-1){//middle
				aL[i]=nextAngle;
				rL[i]=irSensorCm(analogRead(0));
				aR[i-(points-1)]=aL[i];
				rR[i-(points-1)]=rL[i];
				nextAngle-=180/(count-1);
				motor.write(nextAngle);
			} //middle
		
			else if(i>points-1){//right
				aR[i-(points-1)]=nextAngle;
				rR[i-(points-1)]=irSensorCm(analogRead(0));
				nextAngle-=180/(count-1);
				motor.write(nextAngle);
			}//right side		
			delay(delayTime);
			}//motor sensing loop
		Serial.println("");
		motor.write(90);
		
		
		//tell user what was collected
		/*
		Serial.print("Left:");tab();
		for(int i=0;i<points;i++){
			Serial.print(rL[i]);tab();
		}
		Serial.println("");
		
		Serial.print("Right:");tab();
		for(int i=0;i<points;i++){
			Serial.print(rR[i]);tab();
		}
		Serial.println("");
		*/
		
		float mL=slopeCalc(rL,aL,points);
		float mR=slopeCalc(rR,aR,points);
		
		Serial.print("Slopes");tab();
		Serial.print(mL);tab();
		Serial.print(mR);tab();
		Serial.println("");
		
	}//serial loop
	

	delay(1000);
	
} //main loop


float irSensorCm(float rawValue){
	/*receive 0-1023 reading from IR sensor.
	assume near-ideal conditions.
	return distance in [cm].
	*/
	float a=1.04;
	float b=20;
	float c=4348.67;
	return c*a/(rawValue-b);
}

void tab(){
	Serial.print("\t");
}

float avg(float values[],int length){
	float ans=0;
	for(int i=0;i<length;i++)ans+=float(values[i]);
	return ans/float(length);
}

float slopeCalc(float r[],float thetaDeg[], int nPts){
	//convert (r,theta) >>> (x,y)
	float x[nPts];
	float y[nPts];
	for(int i=0;i<points;i++){
		x[i]=r[i]*cos(thetaDeg[i]*3.14159/180);
		y[i]=r[i]*sin(thetaDeg[i]*3.14159/180);
	}//x-y point creation

	//perform simple linear regression
	float xavg=0;
	float yavg=0;
	for(int i=0;i<nPts;i++){
		xavg+=x[i];
		yavg+=y[i];
	}
	xavg/=float(nPts);
	yavg/=float(nPts);
	float a=0;
	float b=0;
	for(int i=0;i<nPts;i++){
		a+=(x[i]-xavg)*(y[i]-yavg);
		b+=(x[i]-xavg)*(x[i]-xavg);
	}
	//return the slope
	return a/b;
}
