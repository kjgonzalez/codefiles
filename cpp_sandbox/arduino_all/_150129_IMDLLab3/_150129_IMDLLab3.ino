/*
objective: write code to first take in an analog signal,
  display it serially to the screen, then output a 
  corresponding PWM signal to a servo.
*/

#include <Servo.h>

Servo m1;


void setup(){
Serial.begin(9600);
m1.attach(3);

delay(500);
Serial.println("Starting");

}//setup

void loop(){

uint16_t a = analogRead(0);
Serial.println(a);
a=map(a,0,1023,1600,2100);
m1.write(a);

delay(100);
}//main loop
