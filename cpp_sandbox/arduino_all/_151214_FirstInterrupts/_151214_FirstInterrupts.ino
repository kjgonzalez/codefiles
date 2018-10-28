/*
Objective: 
learn how to use an interrupt in arduino's code. will 
wire a pin to a pull-down switch, so whenever the 
circuit is switched open and the signal goes to 
ground, a falling edge interrupt will trigger.

UPDATE: works
*/


void trigger(){
	Serial.println("captured");
	/*note, technically this is bad practice,
	  because it is best to set a flag, then
	  quickly exit the routine (do the minimum
	  necessary in an int). */
}

void setup(){
	Serial.begin(9600);


//	two int's exist on UNO: int0(p2), int1(p3)
	attachInterrupt(0, trigger, FALLING); //setup int0, tied to pin2
	Serial.println("starting");
	
}

void loop(){
 // sit and wait
} //main loop


