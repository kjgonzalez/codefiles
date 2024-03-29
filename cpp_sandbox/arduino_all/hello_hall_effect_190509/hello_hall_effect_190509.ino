/*
DateCreated: 190509
Objective: first example of how to connect hall sensor to teensy

Hall effect sensor, PartNo. "A3144 Hall Effect Sensor"

Basic Pinout: 
5V:  5V / VIN
GND: GND / AGND
SIG: 5V - 20k Ohm - SIG - pin12 (signal connected to pull-up resistor)

NOTES: 
1) 20k ohm resistor means that high output from sensor is less than 3V, safe 
    for the teensy 3.1 / 3.2.
2) this code has been tested and confirmed to work, incl. with above pinout
3) the transistor is only attracted to one magnetic pole. thus, it's a monopole
    sensor. 
*/
int pin12 = 12;

void setup(){
    Serial.begin(38400);
    pinMode(pin12, INPUT);
}//setup



void loop() {
    // read the input pin:
    int buttonState = digitalRead(pin12);
    // print out the state of the button:
    Serial.println(buttonState);
    delay(50);        // delay in between reads for stability
}