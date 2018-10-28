/*
objective: make first true feedback loop 
  to control the speed of a DC motor wheel.
  read in a potentiometer value, change speed 
  accordingly. 
  1. read from pot
  2. adjust desired speed
  3. look at current avg velocity
  4. change command
*/


/*
order of programming: 
  get tachometer going
  make avg RPM >>> velocity make sense
  get interrupt and such working
  start making PID.

*/


//common units: cm/g/s
#define WhDiam 6.67
#define Resolution 9 // 360deg/40triggers
#define AIA 9
#define AIB 5
#define BIA 10
#define BIB 6
//float vel=0;
//byte speed=0;

float vd=0;
float kp=.1;

uint8_t lwflag=0;

uint16_t ta=0;
uint16_t tb=0;
uint16_t loopTime=0;
float v=0;

uint16_t refreshInt=1000;
uint16_t currInt=0;

//motor variables
int32_t angle = 0;
int8_t dir=0;
int8_t prevDir=0;
byte vel=0;

void trig(){
	ta=micros();
	loopTime=ta-tb;
	tb=ta;
	lwflag=1;		
}

void addAngle(){
	if(lwflag==1){
		if(dir==1){
			angle+=Resolution;
			prevDir=1;
		}
		else if(dir==2){
			angle-=Resolution;
			prevDir=2;
		}
		else{
			if(prevDir==1)angle+=Resolution;
			else angle-=Resolution;
		}
		
		lwflag=0;
		Serial.println(angle);
	}//if-statement
}//void addAngle

void fwdMove(byte vCommand){
	dir=1;
	M1Comm(vCommand,dir);
}
void bwdMove(byte vCommand){
	dir=2;
	M1Comm(vCommand,dir);
}
void stop(){
	if(vel>0) vel=constrain(vel-50,0,255);
	if(vel==0) dir=0;
	M1Comm(vel,dir);
}

//void slowDown()



void M1Comm(byte velocity,int8_t kjgdir){
	if(kjgdir==1){
		analogWrite(BIB, 0);
		analogWrite(BIA, velocity);
		//Serial.println("fwd");
		}
	else if(kjgdir==2){
		analogWrite(BIA, 0);
		analogWrite(BIB, velocity);
		//Serial.println("bwd");
		}
	else{
		analogWrite(BIA, 0);
		analogWrite(BIB, 0);
		//Serial.println("stop");
		}
	
}

void setup(){
	Serial.begin(9600);
	attachInterrupt(0,trig,CHANGE);
	
	pinMode(AIA, OUTPUT); // set pins to output
	pinMode(AIB, OUTPUT);
	pinMode(BIA, OUTPUT);
	pinMode(BIB, OUTPUT);
	delay(500);
	Serial.println("starting");
	angle=0;
}



//int i1=0;
void loop(){
/*need to first make wheels follow 
  a square wave, then can move on 
  to bigger and better things.
*/

int8_t dir=0;

if(angle < 360) {
	vel=100;
	fwdMove(vel);
}



else{
	stop();
}
addAngle();


// dir=1;
// M1Comm(vel,dir);
// delay(500);
// dir=0;
// M1Comm(vel,dir);
// delay(500);
// dir=-1;
// M1Comm(vel,dir);
// delay(500);
// dir=0;
// M1Comm(vel,dir);
// delay(500);


}//true main loop
