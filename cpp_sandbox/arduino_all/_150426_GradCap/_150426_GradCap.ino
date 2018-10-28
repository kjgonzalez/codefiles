/*
objective: make simple grad cap LED pattern

*/

/*
steps: 
1. initialize pins
2. turn on pair i
3. delay 300 ms
4. turn off pair i
5. increase i, keep between 0,5
6. go to #2
*/
/*
pair 0 : 0,1
pair 1 : 2,3
pair i : i*2,i*2+1
*/
void toggleLED(){
	if(digitalRead(13)==0) digitalWrite(13,1);
	else digitalWrite(13,0);
}//toggleLED

void setup(){
Serial.begin(9600);
delay(100);

pinMode(13,1);
//initialize pins 0 thru 9
for(uint8_t i=0;i<5;i++){
	pinMode(i,1);
	Serial.println(i);
}


} //setup


void loop(){
// Serial.println("hello world");
// toggleLED();
// delay(1000);

// uint8_t ii=0;
for(uint8_t i=0;i<5;i++){
	Serial.println(i);
	digitalWrite(i,1);
	delay(200);
	digitalWrite(i,0);
	toggleLED();
	}//blinking forloop

}//main loop
