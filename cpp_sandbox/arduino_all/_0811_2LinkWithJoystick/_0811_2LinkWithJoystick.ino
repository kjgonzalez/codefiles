/*
main objective: create two-link robot arm with the ability to be controlled
via 2-axis joystick. the user will control the desired x-y coordinate of the 
system, and the system shall move in response to move towards the desired position

there MUST be limits placed on each axis, such as each axis at most being between
1 and 3 inches away from the "origin". 

there MUST also be a reasonable amount of time to allow the system to move to the
desired position.

there will be allowed some system instability, given that initial control will
simply be comprised of P control (not even PD or PID). this is simply for system
simplicity. in the next iteration, perhaps more real system dynamics will be used. 

*/

#include <Servo.h>
#include <math.h>
Servo m1;
Servo m2;


// global variables

int a1=0; //angle 1, in degrees
int a2=0; //angle 2, in degrees
int r1=15.5; //arm 1 length, in cm
int r2=16; //arm 2 length, in cm
int xd=0; //desired x-loc
int yd=0; //desired y-loc

//joystick pins
int xpin=0;
int ypin=1;



void setup(){

Serial.begin(9600); 
delay(3000);
Serial.println("starting...");

m1.attach(3);
m2.attach(5);


//desired initial location
//basically almost stretched out horizontally
m1.write(0);
m2.write(180);



} //setup

void loop(){

while(Serial.available()>0){
	a1=Serial.parseInt();
	a2=Serial.parseInt();
	a2=180-a2;
}


m1.write(a1);
m2.write(180-a2);


delay(300);

}





void getAngles(){
	//changes global variables a1 and a2 from desired x-y loc
	
	double R = sqrt(xd*xd+yd*yd);
	double phi = acos(xd/R);
	double beta=acos((r1*r1+R*R-r2*r2)/(2*R*r1));
	double gamma=acos((r2*r2+R*R-r1*r1)/(2*R*r2));
	
	double aa1=phi+beta; //phi+beta = elbow down, phi-beta = elbow up
	double aa2=beta+gamma;
	
	//convert to degrees
	aa1=aa1*180/3.14159;
	aa2=aa2*180/3.14159;
	
	Serial.println("getAngle results");
	Serial.println("R\tphi\tbeta\tgamma");
	Serial.print(R);tab();
	Serial.print(phi);tab();
	Serial.print(beta);tab();
	Serial.print(gamma);tab(); Serial.println("");
	Serial.print(aa1);tab();Serial.println(aa2);
	
	//constraint because of servo limits
	a1=constrain(aa1,0,180);
	a2=constrain(aa2,0,180);
}


int ConMap(int raw, int inLow, int inHi, int outLow, int outHi){
	return constrain(map(raw,inLow,inHi,outLow,outHi),min(outLow,outHi),max(outLow,outHi));

}

void tab(){
	Serial.print("\t");
}




/* FROM MATLAB:
    % get angles from desired location
    R = sqrt(xd^2+yd^2);
    phi = acos(xd/R);
    beta=acos((r1^2+R^2-r2^2)/(2*R*r1));
    gamma=acos((r2^2+R^2-r1^2)/(2*R*r2));
    a1=phi+beta; %CHANGE HERE FOR ELBOW CONFIG
    a2=beta+gamma;
    %calculate where everything should be:
    x1=r1*cos(a1);
    y1=r1*sin(a1);
    x2=x1+r2*cos(a1-a2); %CHANGE HERE FOR ELBOW CONFIG
    y2=y1+r2*sin(a1-a2); %CHANGE HERE FOR ELBOW CONFIG*/