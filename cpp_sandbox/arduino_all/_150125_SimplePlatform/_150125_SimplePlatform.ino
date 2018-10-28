/*
objective: make a simple mobile platform upon which
  to learn more about obstacle avoidance. will use 
  discontinued china chassis with no wheel feedback, 
  but instead will have two/three distance sensors
  that will try to prevent hitting anything.
  
  part 1 - attain movement ............. DONE
  part 2 - read in from all sensors		.
  part 3 - develop obstacle avoidance
*/


//common units: cm/g/s
#define WhDiam 6.67
#define Resolution 9 // 360deg/40triggers
#define AIA 9
#define AIB 5
#define BIA 10
#define BIB 6
#define speed 120 //byte command, out of 255
#define minDist 18 //cm

//pins
#define IR_Lpin 0
#define IR_Rpin 1
#define trigPin 7
#define echoPin 8
#define buttonPin 2
#define ledPin 13

uint8_t userComm = 0;
uint8_t butInp = 0;
uint8_t bFlag = 0;
void fwdMove(byte vCommand){
	
	MLComm(vCommand,1);
	MRComm(vCommand,1);
}
void bwdMove(byte vCommand){
	
	MLComm(vCommand,2);
	MRComm(vCommand,2);
}
void stop(){
	MLComm(0,0);
	MRComm(0,0);
}
void turnLeft(byte vCommand){
	MLComm(vCommand,2);
	MRComm(vCommand,1);
}
void turnRight(byte vCommand){
	MLComm(vCommand,1);
	MRComm(vCommand,2);
}

void MLComm(byte velocity,int8_t kjgdir){
	if(kjgdir==1){
		analogWrite(BIB, 0);
		analogWrite(BIA, velocity);
		//Serial.print("Lfwd\t");
	}
	else if(kjgdir==2){
		analogWrite(BIA, 0);
		analogWrite(BIB, velocity);
		//Serial.print("Lbwd\t");
	}
	else{
		analogWrite(BIA, 0);
		analogWrite(BIB, 0);
		//Serial.print("Lstop\t");
	}
	
}
void MRComm(byte velocity,int8_t kjgdir){
	if(kjgdir==1){
		analogWrite(AIB, 0);
		analogWrite(AIA, velocity);
		//Serial.println("Rfwd");
	}
	else if(kjgdir==2){
		analogWrite(AIA, 0);
		analogWrite(AIB, velocity);
		//Serial.println("Rbwd");
	}
	else{
		analogWrite(AIA, 0);
		analogWrite(AIB, 0);
		//Serial.println("Rstop");
	}
	
}
uint8_t getCommand(){
	if(Serial.available()==0) return userComm;
	while(Serial.available()>0){
		return Serial.parseInt();
	}
}
void initialPause(){
	Serial.println("Ready");
	while(digitalRead(buttonPin)==0){
		delay(100);
		
	}//pause while loop
	delay(100);
}
void checkforPause(){
	if(digitalRead(buttonPin)==1){
		stop();
		Serial.println("Paused");
		delay(300);
		while(digitalRead(buttonPin)==0){
			delay(100);
			
		}//pause while loop
	}//if statement
}//void checkforPause
uint16_t getLeft(){
	/* receive 0-1023 reading from IR sensor
	   can assume near-ideal conditions.
	   returns distance in [cm]
	*/
	float a = analogRead(IR_Lpin);
	a = 4522.6/(a-20);
	if(a>80) a=80;
	return a; //value is in cm
}
uint16_t getRight(){
	/* receive 0-1023 reading from IR sensor
	   can assume near-ideal conditions.
	   returns distance in [cm]
	*/
	float a = analogRead(IR_Rpin);
	a = 4522.6/(a-20);
	if(a>80) a=80;
	return a;//value is in cm
}
uint16_t getMid(){
	digitalWrite(trigPin,HIGH);
	delayMicroseconds(100);
	digitalWrite(trigPin,LOW);
	uint16_t distcm = pulseIn(echoPin,HIGH);
	distcm=distcm*.0172; //.0172 = 343 cm/us * 1/2
	if(distcm>80) distcm=80;
	return distcm;
}//uint16_t getMid
void blinkPin13(){
	digitalWrite(ledPin,HIGH);
	delay(50);
	digitalWrite(ledPin,LOW);
	delay(50);
	digitalWrite(ledPin,HIGH);
	delay(50);
	digitalWrite(ledPin,LOW);
	delay(49);
}
void tab(){
	Serial.print("\t");
}

uint8_t tooClose(uint16_t cmDistance){
	if(cmDistance<minDist) return 1;
	else return 0;
}

void manualMove(uint8_t ui){
	if(ui==0){
		stop();
	Serial.println(ui);}
	else if(ui==1){
		fwdMove(speed);
		delay(1000);
		stop();
	Serial.println(ui);}
	else if(ui==2){
		bwdMove(speed);
		delay(1000);
		stop();
	Serial.println(ui);}
	else if(ui==3){
		turnLeft(speed);
		delay(1000);
		stop();
	Serial.println(ui);}
	else if(ui==4){
		turnRight(speed);
		delay(1000);
		stop();
	Serial.println(ui);}
}

// MAIN //////////////////////////////////////////////////////////////////

void setup(){
Serial.begin(9600);
pinMode(AIA, OUTPUT); // set pins to output
pinMode(AIB, OUTPUT);
pinMode(BIA, OUTPUT);
pinMode(BIB, OUTPUT);
pinMode(buttonPin,INPUT);
pinMode(ledPin, OUTPUT);
pinMode(trigPin,OUTPUT);
pinMode(echoPin,INPUT);


delay(1000);
initialPause();


// MAIN LOOP /////////////////////////////////////////////////////////////
while(1){
checkforPause();



delay(100);
}//main loop
}//setup



//arduino crap
void loop(){
Serial.println("done");
delay(500);	
}

/*BACKUP - 0130 first working oa, 2/5 score
// START OF OA ALGORITHM

/*
actions, cases:
00 fwd - 000
01 left - 001, 011
02 right - 010, 100, 110
03 backup, turn right - 101
04 backup, 180 - 111
*./

uint16_t L=getLeft();
uint16_t R=getRight();
uint16_t M = getMid();

Serial.print(L);tab();
Serial.print(M);tab();
Serial.println(R);


L=tooClose(L);
M=tooClose(M<<1);
R=tooClose(R);

// check for threshold
if(!L && !M && !R){
	fwdMove(speed);
	//	Serial.println("fwd");
}
else if(!L && R){
	turnLeft(speed);
	//	Serial.println("left");
}
else if(( !L&&M || L&&!M || L&&M ) && !R){
	turnRight(speed);
	//	Serial.println("right");
}

else if(L && !M && R){
	bwdMove(speed);
	delay(400);
	turnRight(speed);
	delay(300);
	stop();
	//Serial.println("Backup,turn");
}
else{
	bwdMove(speed);
	delay(400);
	turnRight(speed);
	delay(600);
	stop();
	//Serial.println("Backup,180");
}


// END OF OA ALGORITHM
*/