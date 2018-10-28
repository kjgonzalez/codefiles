/*
main objective: measure sensor 
input, figure out what it MEANNNSS

*/



void setup(){
Serial.begin(9600);
delay(5000);
Serial.println("Starting...");
Serial.println("");

	Serial.print("cm");
	Serial.print("\t");
	Serial.print("avg");
	Serial.print("\t");
	Serial.println("Pred");
} //setup

void loop(){

while(Serial.available()>0){
	int cm=Serial.parseInt();
	int n=10;
	int avg=0;
	for(int i=0;i<n;i++){
		avg+=analogRead(0);
		delay(1000/n);
	}
	avg=avg/n;
	
	Serial.print(cm);
	Serial.print("\t");
	Serial.print(avg);
	Serial.print("\t");
	Serial.println(irSensorCm(avg));
}

Serial.println(irSensorCm(analogRead(0)));
delay(1000);

} //main loop


//to convert data to cm (kjg testing)


int irSensorCm(float rawValue){
	/*receive 0-1023 reading from IR sensor.
	assume near-ideal conditions.
	return distance in [cm].
	*/
	float a=1.04;
	float b=20;
	float c=4348.67;
	
	return c*a/(rawValue-b);
	
}

