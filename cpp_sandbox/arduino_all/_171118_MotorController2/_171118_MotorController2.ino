/*
objective: use motor controller and pwm pins to drive a dc motor.
  will use outside (wall wart) 5V into the controller, will use 
  pwm pins for logic.
  
  UPDATE: works. also, code from online has been modified to work
  with potentiometer for variable speed.
  
*/


const int AIA = 3;  // (pwm) pin 9 connected to pin A-IA 
const int AIB = 4;  // (pwm) pin 5 connected to pin A-IB 

const int BIA = 5; // (pwm) pin 10 connected to pin B-IA  
const int BIB = 6;  // (pwm) pin 6 connected to pin B-IB 
 
byte speed = 255;  // change this (0-255) to control the speed of the motors 
 
void setup(){
  pinMode(AIA, OUTPUT); // set pins to output
  pinMode(AIB, OUTPUT);
  pinMode(BIA, OUTPUT);
  pinMode(BIB, OUTPUT);
  Serial.begin(9600);
  delay(1000);
  Serial.println("starting");
  
}
 
void loop(){

speed=150;

Serial.print("new cycle: ");
Serial.println(speed);
  forward(); 
  delay(2000);
  backward();
  delay(2000);
  
}
 
void backward()
{
  analogWrite(AIA, 0);
  analogWrite(AIB, speed);
  analogWrite(BIA, 0);
  analogWrite(BIB, speed);
}
 
void forward()
{
  analogWrite(AIA, speed);
  analogWrite(AIB, 0);

  analogWrite(BIA, speed);
  analogWrite(BIB, 0);
}