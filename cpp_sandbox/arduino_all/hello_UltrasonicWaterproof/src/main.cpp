#include <Arduino.h>

class UltrasonicA02YYUW
{
public:
    uint8_t buf[4];
    HardwareSerial *ser;
    UltrasonicA02YYUW(HardwareSerial &serial) 
    {
        ser = &serial; 
        buf[0]=0;buf[1]=0;buf[2]=0;buf[3]=0;
    }
    void update()
    {
        // update buffers. note: takes about 16us with TeensyLC
        ser->write(0xFF);
        buf[0] = ser->read();
        buf[1] = ser->read();
        buf[2] = ser->read();
        buf[3] = ser->read();
    }
    uint16_t dist_mm() { return buf[1]*256+buf[2]; }
    bool isValid()
    {
        bool test1 = ((buf[0]+buf[1]+buf[2])&0xFF) == buf[3];
        bool test2 = buf[0] == 0xFF;
        return test1 && test2;
    }
};

UltrasonicA02YYUW sens(Serial1);

void setup() {
    pinMode(LED_BUILTIN,OUTPUT);
    Serial.begin(115200);
    Serial1.begin(9600);
    delay(100);
    Serial.println("starting");
}

void loop() {
    sens.update();
    Serial.printf("pinged: %d mm (valid? %d)\n",
        sens.dist_mm(), sens.isValid()
    );

    digitalWrite(LED_BUILTIN,1);
    delay(10);
    digitalWrite(LED_BUILTIN,0);
    delay(1990);
}