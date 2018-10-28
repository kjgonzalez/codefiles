/*
starting fresh in order to build good tachometer.
trouble with previous: erratic behavior due to 
environmental lighting changes.

*/

int smin=0;
int smax=0;
int smid=0;
int sval=0;
int sloc=0;
int prevSNS=0;
int currSNS=0;
int countSNS=0;

int button=12;
int currSerial=0;
int currBTN=0; //current state of button
int prevBTN=0; //previous state of button

float hz=0;
float prevkk=0;
float currkk=0;
float testpkk=0;
float testckk=0;

int latchBTN=0;
int n=0;
int prevTime=0;
int loopTime=0;
int sampleSize=3;
int baseDelay=50; //ms



void setup(){
	Serial.begin(9600);
	//pinMode(light,OUTPUT);
	pinMode(button,INPUT);
	delay(5000);
	Serial.println("starting...");

}//setup

void loop(){

sval=analogRead(sloc); //read in photo-res value

//Serial.print(analogRead(sloc));
//Serial.print("\t");
currBTN=digitalRead(button); //read in if button is currently pressed

//commence latch ///////////////
if(prevBTN==0 && currBTN==1){
	Serial.print("BTN latch");
	tab();
	latchBTN=1;
}//0 1
else{latchBTN=0;}
prevBTN=currBTN;
//end latch ////////////////////


// BTN LATCH ACTIONS //////
if(latchBTN==1){
	if(n==0){
		//save smin
		smin=analogRead(sloc);
		n++;
	}
	else if(n==1){
		//save smax
		smax=analogRead(sloc);
		smid=(smax+smin)/2;
		n++;
		prevkk=millis(); //help initialize RPM counter
		testpkk=millis();
	}
	else if(n==2){
		//print out results
		Serial.println("");
		Serial.println("items");
		Serial.print(smin);tab();
		Serial.print(smax);tab();
		Serial.print(smid);
		Serial.println();
		n++;
		
	}
}//latch has been pressed, will do stuff
// BTN LATCH ACTIONS END //



//photo resistor latching // 

if(n==3){
	int timehold=0;
	
	currSNS=eitheror(sval,smid);
	
	////// SNS latch //////////
	if(prevSNS==0 && currSNS==1){
		currkk=millis();
		testckk=millis();
		Serial.println("");
		//latchSNS=1;
		countSNS++;
		//Serial.print(currkk);
		//Serial.print(" SNS Latch");tab();
		hz=1000/(currkk-prevkk);
		prevkk=currkk;
		
		Serial.print("Hz: ");
		Serial.print(hz);Serial.print(" ");
		Serial.print(countSNS); tab();
		
	}
	else {}//latchSNS=0;
	prevSNS=currSNS;
	// end SNS latch //////////
}//time to do latch on photo resistor


if(countSNS==(sampleSize)) {
	countSNS=0;
	
	
	hz=sampleSize*1000/(testckk-testpkk);
	Serial.print("Hz2: ");
	Serial.print(hz);
	testpkk=testckk;
	
}
	




//Serial.println("");
delay(baseDelay);
}//main loop



void tab(){
	Serial.print("\t");
}


int eitheror(int var,int threshold){
	if(var>threshold)return 1;
	else return 0;
}

