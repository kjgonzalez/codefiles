/*
Bicycle Odometer
board: Teensy LC ("A")

Using the eeprom of the teensy, keep track of bicycle distance traveled with low power usage

NOTES: 
* pc-based serial client available at echo_test_181117
* TeensyLC has EEPROM of 128B. 
* 

float = 4B
unsigned long long (uint64_t) = 8B

STAT DESCRIPTION
done eeprom read/writable?
done write name to eeprom
done can you communicate via serial? 
done 0: debug, cause wheel turn
done 9: debug, fully reset information
done 1: get info
done 2: reset trip
done 3: set wheel diameter (will ask for value & light up)
done create state machine (active / sleep states)
done initialize eeprom with right values
inpr able to go into low power mode? 
???? perhaps have eeprom_writes as part of datastruct?
???? how long does a set of AA batteries last? 
???? can hall sensor be put as interrupt?
???? can interrupt wake teensy from sleep?
???? is there a risk if you add llu and uint8?
???? 

*/
asm(".global _printf_float"); // required to allow floats in sprintf
#include <EEPROM.h>
#include <LibPrintf.h>
#include <Snooze.h> // maybe not needed here? 
#define ADDR_OWNER 0 // 20, char[20] (should be read only)
#define ADDR_DIST 20 // 8, long long unsigned (uint64_t), max dist ~184 trillion km (int32 only about 42k km)
#define ADDR_TRIP 28 // 8, long long unsigned (uint64_t)
#define ADDR_DIAM 36 // 1, uint8_t
#define PIN_SENSOR 2
#define PIN_LED 13
#define T_WAIT_COMM 30 // ms. true wait time will be 120000, 2 minutes
#define T_WAIT_REACT 10000 // ms. true wait time will be 5000, 5 seconds
#define T_WAIT_SLEEP 5000 // ms. true wait time will be 86399000, 24 hours-1 second
#define nl "\n"
// #define ADDR_SPDM 37 // 1, float // won't be used

struct bikedata{
    unsigned long long distcm;
    unsigned long long tripcm;
    uint8_t diamcm;
} dat;
bool flag_interrupt=false;
bool led_state=false;
// struct bikedata dat;

void eeprom2bikedata(){
    // read from eeprom and put data into ram
    EEPROM.get(ADDR_DIST,dat.distcm);
    EEPROM.get(ADDR_TRIP,dat.tripcm);
    EEPROM.get(ADDR_DIAM,dat.diamcm);
}

void bikedata2eeprom(){
    EEPROM.put(ADDR_DIST,dat.distcm);
    EEPROM.put(ADDR_TRIP,dat.tripcm);
    EEPROM.put(ADDR_DIAM,dat.diamcm);
}

void cb_wheelturn(){
    dat.distcm+= dat.diamcm;
    dat.tripcm+=(unsigned long long) dat.diamcm;
    // printf("int" nl);
    flag_interrupt=true;
    led_state=!led_state;
    digitalWrite(PIN_LED,led_state);
}

void c0_wheelturn(){ Serial.println("DEBUG: wheel turn"); cb_wheelturn(); }

void read_region(int start, int lim){
    if(lim<start) return;
    printf("EEPROM:" nl);
    for(int i=start;i<lim;i++){ printf("%3d: %d" nl,i,EEPROM.read(i)); }
}

void c9_misc(){
    // set baseline and program eeprom
    dat.distcm = 100000; //1km
    dat.tripcm = 100000; // 1km
    dat.diamcm   = 213; // cm
    printf("written to eeprom" nl);
}

void c8_misc(){
    printf("old value:" nl);
    print_info();
    printf("from EEPROM:" nl);
    eeprom2bikedata();
    print_info();
}
void print_info(){ 
    printf("Dist [km]: %0.3f" nl,(float)dat.distcm/100000);
    printf("Trip [km]: %0.3f" nl,(float)dat.tripcm/100000);
    printf("Diam [m] : %d" nl,dat.diamcm);
    char buf[20];
    EEPROM.get(ADDR_OWNER,buf);
    Serial.print("Owner: ");printf(buf);printf(nl);
    }
void c2_tripreset(){ 
    printf("Resetting Trip" nl);
    dat.tripcm=0.0;
    }
void c3_setdiam(uint8_t diamcm){ 
    printf("Prev Diam: %d" nl,dat.diamcm);
    dat.diamcm = diamcm;
    printf("New Diam : %d" nl,dat.diamcm);
    }



class StComm:State{public:
    unsigned long t_last_comm;
    bool isactive;
    String command="";
    StComm(){
        t_last_comm=millis();
        isactive=false;
    }
    void enter(){
        printf("state: comm" nl);
        isactive=true;
        t_last_comm=millis();
    }
    void exit(){
        isactive=false;
    }
    st_t runloop(){
        if(!isactive) enter(); // re-initialize
        while(Serial.available()>0){
        // digitalWrite(13,HIGH);
        // delay(50);
        // digitalWrite(13,LOW);

        command = Serial.readString();
        t_last_comm = millis();
        if(command.length()==2){
            Serial.println("---");
            switch(command.charAt(0)){
                case '1': {print_info();break;}
                case '2': {c2_tripreset();break;}
                // DEBUG--------------------------
                case '8': {c8_misc();break;}
                case '9': {c9_misc();break;}
                case '0': {c0_wheelturn();break;}
                }//switch
            }//if-cmd=2
        else if(command.charAt(0)=='d'){
            c3_setdiam(command.substring(1,command.length()).toInt());
        }
        else if(command.charAt(0)=='r' && command.indexOf(',')!=-1){
            int ind = command.indexOf(',');
            int val1=command.substring(1,ind).toInt();
            int val2=command.substring(ind+1,command.length()).toInt();
            //printf("val1: %d. val2: %d" nl,val1,val2);
            read_region(val1,val2);
        }
        else{
            Serial.print("not recognized: ");Serial.print(command);
            }//else
    }//while data available

    if(millis()-t_last_comm>T_WAIT_COMM){
        exit();
        return STreactive;
        }
    else{return STcomm;}
    } //runloop
};

class StReactive:State{public:
    unsigned long t_last_comm;
    bool hasprinted;
    bool isactive;
    StReactive(){t_last_comm=millis();isactive=false;}
    void enter(){
        printf("state: reactive" nl);
        t_last_comm=millis();
        isactive=true;
        }
    void exit(){isactive=false;}
    st_t runloop(){
        if(!isactive)enter();
        if(flag_interrupt){
            t_last_comm=millis();
            flag_interrupt=false;
            printf("reactive: int detected" nl);
            }

        if(millis()-t_last_comm>T_WAIT_REACT){
            print_info();
            exit();
            return STsleep;
        }
        else{return STreactive;}
    }//runloop
};

// SnoozeDigital digital;
// SnoozeTimer timer;
// // SnoozeBlock config_teensyLC(lc5vBuffer,digital,timer);
// SnoozeBlock config_teensyLC(digital,timer);


class StSleep{public:
    bool isactive;
    bool newinfo=false;
    int who; // which config is waking up the clock
    StSleep(){isactive=false;}
    void enter(){
        printf("state: sleep" nl);
        isactive=true;
        if(stateprev==STsave){
            printf("coming from save state" nl);
            newinfo=false;
        } else {newinfo=true;}

        }//enter
    void exit(){isactive=false;}
    st_t runloop(){
        if(!isactive)enter();
        if(flag_interrupt){
            printf("sleep: int detected" nl);
            flag_interrupt=false;
            exit();
            return STreactive;
        }//if-flag_interrupt
        

        // digitalWrite(13,HIGH);
        // delay(ledtime);
        // digitalWrite(13,LOW);
        //delay(950);
        // who = Snooze.deepSleep(config_teensyLC);
        // printf("woken by : %d",who);
        // be able to pull out of sleep
        // if(interrupt){ exit();return STreactive; }
        // else {return STsleep;}
        
        // if have been able to sleep uninterrupted, decide where to go next
        exit();
        if(newinfo) return STsave;
        else return STsleep;
    }
};

class StSave{public:
    /* Write current information to eeprom. NOTE: do not actually write until sleep class 
        functioning correctly!  
    write all values into eeprom, first putting into separate buffer to avoid unlikely event of 
        race condition. immediately return to sleep state
    */
    bool isactive;
    unsigned long long temp_distcm;
    unsigned long long temp_tripcm;
    uint8_t temp_diamcm;

    StSave(){isactive=false;}
    void enter(){
        printf("state: save" nl);
        isactive = true;
    }
    void exit(){
        isactive=false;
    }
    st_t runloop(){
        if(!isactive)enter();
        exit();
        printf("written" nl);
        return STsleep;
    }
};




st_t res = STcomm;
st_t state = STcomm;
// Snoozelc5vBuffer lc5vBuffer;

// initialize states
StComm st_comm;
StReactive st_reactive;
StSleep st_sleep;

StateMachine sm;

// ==================================== setup ====================================
void setup() {
    Serial.begin(115200);
    // while(!Serial){;} // wait for serial to init // should not wait for serial to init
    pinMode(PIN_LED,OUTPUT); // use led
    printf("Ready" nl);
    Serial.setTimeout(10);
    eeprom2bikedata();
    print_info();
    // digital.pinMode(2,INPUT_PULLUP,RISING);
    // timer.setTimer(5000); // [ms]
    attachInterrupt(digitalPinToInterrupt(2),cb_wheelturn,FALLING); // change to rising, see if makes difference
}

void loop() {
    printf("loop" nl);
    delay(1000);
    // switch (state) {
    // case (STcomm): {res=st_comm.runloop();break;}
    // case (STreactive): {res=st_reactive.runloop();break;}
    // case (STsleep): {res=st_sleep.runloop();break;}
    // default:{
    //     printf("using default switch statement in loop" nl);
    //     res = STcomm;
    //     break;
    //     } // switch-default. infinite loop, effectively off...
    // }//switch
    // if(res!=state){
    //     stateprev=state;
    //     state=res;
    // }
}//loop