#include <Arduino.h>

// put function declarations here:
#define PIN_LED 13
#define PIN_SENSOR PIN_A9 // TeensyLC physical pin23

#define T_CYCLE 2000
#define T_ON 1
void setup() {
    // put your setup code here, to run once:
    pinMode(PIN_LED, OUTPUT);
    Serial.begin(9600); // could be 115200 as well
    while(!Serial); // need to wait for native USB port
    delay(100);
}

void loop() {
    int val = analogRead(PIN_SENSOR);
    Serial.println(val);

    // Serial.println("Hello from Arduino!");

    digitalWrite(PIN_LED, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(T_ON);               // wait for a second
    digitalWrite(PIN_LED, LOW);    // turn the LED off by making the voltage LOW
    delay(T_CYCLE-T_ON);               // wait for a second
}
