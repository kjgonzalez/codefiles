/*
learn how to use arrays. if possible, 
also learn how to use pointers 

*/

int asize=12;

int names[3]; 



int length= sizeof(names)/sizeof(names[0]);


void setup(){
	delay(5000);
	Serial.begin(9600);
	Serial.println("starting...");
	Serial.print("length of array: ");tab();
	Serial.print("done");

	for (int i=0;i<3;i++){
		names[i]=0;
	}
	
	Serial.println(length);
	Serial.println(lengthnew(names));
	

}//setup

void loop()
{

  /* add main program code here */

}



void tab(){
	Serial.print("\t");
}


int lengthnew(int arrayName[]){
	return sizeof(arrayName)/sizeof(arrayName[0]);
	
}

