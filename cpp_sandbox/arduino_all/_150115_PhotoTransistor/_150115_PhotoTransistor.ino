/*
objective: try to get photo transistor to function properly.
first, try to read what is coming in through adc. then digital.
then interrupt.

UPDATE: works. follow specsheet (but not too closely, hahahaha)
*/

void trigger(){
	Serial.println("captured");
	/*note, technically this is bad practice,
	  because it is best to set a flag, then
	  quickly exit the routine (do the minimum
	  necessary in an int). */
}

void setup(){
	pinMode(5,INPUT);
	attachInterrupt(0,trigger,FALLING);
	
	Serial.begin(9600);
	delay(500);
	Serial.println("starting");


}

void loop(){
// 	Serial.print(digitalRead(5));
// 	Serial.print("\t");
// 	Serial.println(analogRead(0));
// 
// 	delay(100);

}
