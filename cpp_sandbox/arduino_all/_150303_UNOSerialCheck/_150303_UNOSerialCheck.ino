/*
objective: check that visual 
  micro can still compile
  crap for the board, not sure
  why the other stuff wasn't
  working...

  current functionality: 
  act as a relay between incoming
  serial values from TWI, to 
  the computer montior via USB.

  
  UPDATE: works
*/


void setup(){
Serial.begin(9600);
delay(1000);
Serial.println("starting");

/*
kjg reminder: Serial library uses 8 bit, no parity, 1 stop bit. 
 also, 28800 baud works rather nicely, but you should see the fastest, 
 most reliable speed available.
*/


}

void loop(){

while(Serial.available()>0){
	Serial.write(Serial.read()); //take 
	
}

}
