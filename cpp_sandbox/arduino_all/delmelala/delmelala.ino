void setup(){
Serial.begin(28800);
delay(1000);
Serial.println("starting");

}

void loop(){

while(Serial.available()>0){
	Serial.write(Serial.read());
	
}

}
