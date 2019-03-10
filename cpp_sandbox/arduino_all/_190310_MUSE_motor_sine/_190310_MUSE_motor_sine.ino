/*
Author: Kris Gonzalez
Objective: have the teensy control the motors while mounted ON Muse. musebot 
    should be able to wire the power properly to the motor controller, and 
    thus allow the motors to turn. in this code, will SIMPLY get motors to 
    turn automatically, forward and back, in square sine wave fashion.
*/

#define p1a 3
#define p1b 4
#define p2a 5
#define p2b 6
#define pled 13
void setup(){
    Serial.begin(38400);
    // pinMode(p1a,1);
    // pinMode(p1b,1);
    // pinMode(p2a,1);
    // pinMode(p2b,1);
    pinMode(pled,1);
    delay(2000);
    Serial.println("Hello world");
}//void setup

void loop(){
    Serial.println("test");    
    // motor turn dir1
    analogWrite(p1a,255);
    analogWrite(p1b,0);
    delay(1000);
    
    //motor turn dir2
    analogWrite(p1a,0);
    analogWrite(p1b,255);
    delay(1000);

    // motor stop
    analogWrite(p1a,0);
    analogWrite(p1b,0);
    delay(1000);

    //blink
    digitalWrite(pled,1);
    delay(100);
    digitalWrite(pled,0);
    delay(100);
    

}//void loop


//eof
