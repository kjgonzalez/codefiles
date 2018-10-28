/*code objective: measure light pulses as something goes in between a light emitter and sensor
  thus, will be able to measure something like RPM's, etc.
  
*/

//NOTE: CORRECT SETUP: 
// HIGH >> PH-RES >> SENS-PIN >> RESISTOR >> GND
//produces: dark = low values, bright = high

//global varspace
int smax=0;
int smin=0;
int smid=0;
int sloc=0;  //sensor location
int eloc=12; //emitter location
int sval=0;
int prevLED=0;

//temp vars
int prevTime=0;
int currTime=0;
int loopTime=0;
int waitTime=0;

void setup(){
  //initialize system
  Serial.begin(9600);
  delay(3000);
  Serial.println("start");
  pinMode(eloc,OUTPUT);
  
  //get "off" reading
  smin=analogRead(sloc);
  
  //get "on" reading
  digitalWrite(eloc,HIGH);
  delay(600);
  smax=analogRead(sloc);
  delay(200);
  digitalWrite(eloc,LOW);
  delay(200);
  //setup "threshold"
  smid=(smax+smin)/2;
  
  Serial.println("min \t max \t mid");
  Serial.print(smin);  Serial.print("\t");
  Serial.print(smax);  Serial.print("\t");
  Serial.println(smid);
  //loopTime setup
  currTime=millis();
  
  //LED setup
  sval=analogRead(sloc);
  if(sval<=smid)prevLED=0; //LED on
  else if(sval>smid)prevLED=1; //LED off
  } //setup

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

void loop(){

sval=analogRead(sloc);
Serial.println(sval);
delay(250);

}//main loop
