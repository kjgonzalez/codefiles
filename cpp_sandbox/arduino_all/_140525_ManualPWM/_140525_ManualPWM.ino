/*
main objective: use serial input to send a pwm 
signal to the motor and try to perfectly zero out the 
strange movement that it has.

update: seems to zero out at 1715ms pulse "PPM" 
*/
#include <Servo.h>
Servo motor;


void setup(){
Serial.begin(9600);
motor.attach(3);
motor.write(114);

delay(3000);
Serial.println("starting...");




} //setup

void loop(){

while(Serial.available()>0){
int n=Serial.parseInt();
motor.write(n);
Serial.print("Writing ");
Serial.println(n);

}//serial input loop

delay(1);
}//main loop


