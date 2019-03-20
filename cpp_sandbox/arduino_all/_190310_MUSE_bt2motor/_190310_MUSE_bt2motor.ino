/*
Author: Kris Gonzalez
Objective: control motors from bluetooth while teensy is mounted on Musebot. 
    The overall objective is to be able to move motors fwd/bwd/left/right, 
    but this can be achieved piece-by-piece as follows:
1. get wasd response from bluetooth
2. map wasd to (m1-fwd,m1-bwd,m2-fwd,m2-bwd)
3. map wasd to fwd,bwd,left,right

ASSUMPTIONS: 
    * as of 190310: m1 = left, m2 = right
    * (+) vel = fwd
*/

//define pinouts here
#define pled 13
#define p1a 3
#define p1b 4
#define p2a 5
#define p2b 6

void motor1(int vel){
    /* Receive command between [-255,255] to translate into magnitude & 
        direction of motor1 velocity. 
    */
	vel=constrain(vel,-255,255);
	if(vel>0){
		//want to rotate one way
		analogWrite(p1a,0);
		analogWrite(p1b,vel);
	}//vel>0
	else if(vel<0){
		analogWrite(p1a,abs(vel));
		analogWrite(p1b,0);
	}//vel<0
	else{
		analogWrite(p1a,0);
		analogWrite(p1b,0);
	}//vel=0
}//

void motor2(int vel){
    /* Receive command between [-255,255] to translate into magnitude & 
        direction of motor1 velocity. 
    */
	vel=constrain(vel,-255,255);
	if(vel>0){
		//want to rotate one way
		analogWrite(p2a,0);
		analogWrite(p2b,vel);
	}//vel>0
	else if(vel<0){
		analogWrite(p2a,abs(vel));
		analogWrite(p2b,0);
	}//vel<0
	else{
		analogWrite(p2a,0);
		analogWrite(p2b,0);
	}//vel=0
}//

void setup(){
    Serial.begin(38400);
    Serial1.begin(38400);
    delay(2000);
    Serial.println("musebot start");
    
}//setup

void loop(){
    char inp [3];
    // int inByte;
    int tdelay=40;
    int speed = 200;
    if(Serial1.available()>0){
        
        // inByte=Serial1.read();
        Serial1.readBytes(inp,3);
        if(inp[0]=='w'){
            Serial.println("bt: w");
            motor1(speed);
            motor2(speed);
            delay(tdelay);

        }//if_w
        else if(inp[0]=='a'){
            Serial.println("bt: a");
            motor1(0);
            motor2(speed);
            delay(tdelay);
        }//if_a
        else if(inp[0]=='s'){
            Serial.println("bt: s");
            motor1(-speed);
            motor2(-speed);
            
            delay(tdelay);
        }//if_s
        else if(inp[0]=='d'){
            Serial.println("bt: d");
            motor1(speed);
            motor2(0);
            
            delay(tdelay);
        }//if_d

    }//if_bt_data_available
    motor1(0);
    motor2(0);
}//mainloop