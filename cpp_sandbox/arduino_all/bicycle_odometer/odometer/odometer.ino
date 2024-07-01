/*
Bicycle Odometer
board: Teensy LC ("A")

Using the eeprom of the teensy, keep track of bicycle distance traveled with low power usage

NOTES: 
* HOW TO USE THIS CODE: 
  * open solution in visual studio
  * use "localtest.cpp" to test ideas out locally
  * be careful with teensy space usage! only has 63488B for program, 8192B for RAM
* pc-based serial client available at echo_test_181117
* TeensyLC has EEPROM of 128B. 
* canyon grizl 6 has wheel circumference of 212cm
* uint8_t c_wheel = 212
* uint32_t n_turns >> max value is 4294967295, equivalent distance is 9.1 million km
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
#include <LibPrintf.h>
#define string String
//#include <String>

//using String as string;

// 
// 
// 
//#include <EEPROM.h>
// #include <Snooze.h> // maybe not needed here? 
#include "StateMachine.hpp"

#define ADDR_OWNER 0 // 20, char[20] (should be read only)
#define ADDR_DIST 20 // 8, long long unsigned (uint64_t), max dist ~184 trillion km (int32 only about 42k km)
#define ADDR_TRIP 28 // 8, long long unsigned (uint64_t)
#define ADDR_DIAM 36 // 1, uint8_t
#define PIN_SENSOR 2
#define PIN_LED 13
#define T_WAIT_COMM 30 // ms. true wait time will be 120000, 2 minutes
#define T_WAIT_REACT 10000 // ms. true wait time will be 5000, 5 seconds
#define T_WAIT_SLEEP 5000 // ms. true wait time will be 86399000, 24 hours-1 second

// #define ADDR_SPDM 37 // 1, float // won't be used

struct Counter {
    uint32_t n_turns = 47170; // approx. 100km
    uint8_t c_wheel = 212; // canyon bicycle
    float dist_traveled_km(){ 
        float km = (float)(n_turns * c_wheel) / 1e5;
        return km;
    }
};

Counter cm;

void cb_wheelturn() {
    printf("turn!\n");
    cm.n_turns++;
}


// ==================================== setup ====================================
void setup() {
    Serial.begin(115200);
    Serial.setTimeout(10);
    pinMode(PIN_LED,OUTPUT); // use led
    attachInterrupt(digitalPinToInterrupt(2), cb_wheelturn, FALLING); // change to rising, see if makes difference
    printf("Ready\n");

    // initializations
    StateActive st_active;
    StateMachine sm;
    sm.start(&st_active);
    // main loop


    while (true) {
        sm.mainloop();
    }


} // setup

void loop() {
    printf("done\n");
    delay(1000);
}//loop

