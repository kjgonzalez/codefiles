/*
main objective: play with new joystick and output command to two servos.
essentially, this 2-axis joystick is simply comprised of two potentiometers.
will configure.

UPDATE: position control good. velocity control okay. DONE

*/

#include <Servo.h>
Servo mx;
Servo my;

int xpin=0;
int ypin=1;

int mode=1;
//1 = position
//2 = velocity (with limits)



int xang=90;
int yang=90;


void setup(){

Serial.begin(9600);
delay(3000);
Serial.println("starting...");

mx.attach(3);
my.attach(5);

if(mode!=1){
	mx.write(xang);
	my.write(yang);
	delay(100);
}

}//setup

void loop(){

//read in joystick position
int xval=analogRead(xpin);
int yval=analogRead(ypin);


if(mode==1){//position control
	mx.write(ConMap(xval,0,1024,0,180));
	my.write(ConMap(yval,0,1024,0,180));
}

else {//velocity control
	
	//desired velocity value
	int lims=2;
	xval=ConMap(xval,0,1004,-lims,lims);
	yval=ConMap(yval,0,1004,-lims,lims);
	
	//new desired position value
	xang=constrain(xang+xval,0,180);
	yang=constrain(yang+yval,0,180);	

	//send out what current velocity is	
	Serial.print(xval);
	Serial.print(",");
	Serial.println(yval);
	
	//send command, with limit between 0 and 180
	mx.write(xang);
	my.write(yang);
}






//give an input to show current joystick position
while(Serial.available()>0){
	int a=Serial.parseInt();
	Serial.print(xval); tab();
	Serial.print(yval);
	Serial.println("");	
}


delay(10);

}//main loop


void tab(){
	Serial.print("\t");
}

int ConMap(int raw, int inLow, int inHi, int outLow, int outHi){
return constrain(map(raw,inLow,inHi,outLow,outHi),outLow,outHi);	
}