/*
objective: take first initial measurements with
  accelerometer to make sure that it works, and 
  understand what "0G", "SL", and "ST" features
  actually entail (and how to use them)
 
UPDATE: IT WORKS!!!
however, seem to have issues when translating back to g's
*/


#define zeroGpin 2
#define b1Pin 6
#define b2Pin 8
#define STpin 4
#define ledPin 13
#define nReadings 16 //ensure always a multiple of two for easy division
#define minLimit 30
#define recordTime 250 //ms, controls array size
uint16_t xval=0;
uint16_t yval=0;
uint16_t zval=0;
uint16_t xprev=0;
uint16_t yprev=0;
uint16_t zprev=0;



uint16_t bigarr[3][recordTime];

void tab(){
	Serial.print("\t");
}

void nline(){
	Serial.println("");
}
void getNewValues(){
	
	xprev=xval;
	yprev=yval;
	zprev=zval;
	
	xval=0;
	yval=0;
	zval=0;
	for(int i=0;i<nReadings;i++){
		xval+=analogRead(0);
		yval+=analogRead(1);
		zval+=analogRead(2);
	}
	xval=xval>>4;
	yval=yval>>4;
	zval=zval>>4;
}//void getNewValues
void selfTest(){
	//note: sensor must be upside down for this test
	uint8_t n = 0;
	while(Serial.available()>0){
		n = Serial.parseInt();
	}
	if(n==1){
		digitalWrite(STpin,HIGH);
		delay(1000);
		digitalWrite(STpin,LOW);
	}
}//void selfTest
uint8_t delta(uint16_t v1,uint16_t v2, uint8_t lim){
	uint16_t result=0;
	if(v1>v2) result = v1-v2;
	if(v2>v1) result = v2-v1;
//	else return 0;
	if(result>lim) return 1;
	else return 0;
}
void printValues(uint8_t threshold){
	
	uint8_t lim = threshold;

	uint16_t deltax=delta(xval,xprev,lim);
	uint16_t deltay=delta(yval,yprev,lim);
	uint16_t deltaz=delta(zval,zprev,lim);

	if((deltax || deltay || deltaz)){
		Serial.print(millis()); tab();
		
		if(deltax) Serial.print(xval);
		else Serial.print(".");
		tab();

		if(deltay) Serial.print(yval);
		else Serial.print(".");
		tab();
		
		if(deltaz) Serial.print(zval);
		else Serial.print(".");
		//	tab();

		nline();
	}
}

void printVal0G(){
	uint8_t zeroGval=digitalRead(zeroGpin);
	if(zeroGval==1) Serial.println("zero G");
}


void blink(uint8_t pin){
	digitalWrite(pin,HIGH);
	delay(200);
	digitalWrite(pin,LOW);
	delay(200);
	digitalWrite(pin,HIGH);
	delay(200);
	digitalWrite(pin,LOW);
}

void recordData(){
	if(digitalRead(b1Pin)){
		blink(ledPin);
		digitalWrite(ledPin,HIGH);
		for(uint16_t i=0;i<recordTime;i++){
			getNewValues();
			bigarr[0][i]=xval;
			bigarr[1][i]=yval;
			bigarr[2][i]=zval;
			delay(1);
		}//forloop to record
		Serial.println("done");		
		blink(ledPin);
	}
}//void recordData
	
void printData(){
	if(digitalRead(b2Pin)){
		blink(ledPin);
		Serial.println("");
		for(uint16_t i=0;i<recordTime;i++){
			Serial.print(bigarr[0][i]);tab();
			Serial.print(bigarr[1][i]);tab();
			Serial.print(bigarr[2][i]);nline();
		}//forloop
	}//if statement
}//void printData

void setup(){
Serial.begin(9600);
pinMode(zeroGpin,INPUT);
pinMode(STpin,OUTPUT);
pinMode(b1Pin,INPUT);
pinMode(b2Pin,INPUT);
pinMode(ledPin,OUTPUT);




delay(500);
Serial.println("starting");


}

void loop(){
selfTest();
getNewValues();
printValues(minLimit);
//printVal0G(); //the zero G pin only tells 
// you if the chip is in free-fall

recordData();
printData();


delay(1);
} //main loop
