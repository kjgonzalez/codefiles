/*
k251006: initial code to get a basic behavior out of ILI9341
future pending: SD card read/write

library dependencies: 
	paulstoffregen/XPT2046_Touchscreen@0.0.0-alpha+sha.26b691b2c8
	adafruit/Adafruit ILI9341@^1.6.2
	adafruit/Adafruit GFX Library@1.12.1


wiring: 
TEENSY LC       | TFT ILI9341
board ---(bread)|----(bread)-
VIN       (r01) | 01 (r17) VCC
RGND      (r02) | 02 (r18) GND
P10-cs0   (L12) | 03 (r19) CS
P02       (L04) | 04 (r20) RESET
P03       (L05) | 05 (r21) DC (data/cmd line)
P11-mosi0 (L13) | 06 (r22) SDI(MOSI)
P13-sck0  (r14) | 07 (r23) SCK
VIN       (r01) | 08 (r24) LED
P12-miso0 (L14) | 09 (r25) SDO(MISO)
P13-x2    (r14) | 10 (r26) T_CLK ------|
P06       (L08) | 11 (r27) T_CS        |
P11-x2    (L13) | 12 (r28) T_DIN-mosi  | TOUCH
P12-x2    (L14) | 13 (r29) T_DO-miso   |
n/a       (xxx) | 14 (r30) T_IRQ ------|





*/
#include <Arduino.h>

#include <SPI.h>
#include "Adafruit_GFX.h"
#include "Adafruit_ILI9341.h"
#include "XPT2046_Touchscreen.h"


#define TFT_DC   3
#define DSP_CS  10
#define TFT_RST  2
#define TCH_CS   6

//SPIClass touchscreenSPI = SPIClass(SPI);
Adafruit_ILI9341 tftdisp = Adafruit_ILI9341(DSP_CS,TFT_DC,TFT_RST);
XPT2046_Touchscreen tfttouch(TCH_CS);


#define SCREEN_WIDTH 320
#define SCREEN_HEIGHT 240
#define FONT_SIZE 2

unsigned long testFillScreen();
unsigned long testText();
unsigned long testLines(uint16_t color);
unsigned long testFastLines(uint16_t color1, uint16_t color2);
unsigned long testRects(uint16_t color);
unsigned long testFilledRects(uint16_t color1, uint16_t color2);
unsigned long testFilledCircles(uint8_t radius, uint16_t color);
unsigned long testCircles(uint8_t radius, uint16_t color);
unsigned long testTriangles();
unsigned long testFilledTriangles();
unsigned long testRoundRects();
unsigned long testFilledRoundRects();


void setup() {

    Serial.begin(115200);
    delay(1);
    Serial.println("ILI9341 Test");
    
    pinMode(DSP_CS,OUTPUT);
    pinMode(TCH_CS,OUTPUT);
    digitalWrite(DSP_CS,HIGH);
    digitalWrite(TCH_CS,HIGH);

    tftdisp.begin();
    tfttouch.begin();
    tfttouch.setRotation(1);


    Serial.print(F("Triangles (filled)       "));
    Serial.println(testFilledTriangles());
    Serial.println(F("Done!"));
    for(uint8_t rotation=0; rotation<4; rotation++) {
        tftdisp.setRotation(rotation);
        testText();
        delay(1000);
    }
}


void loop() {
    if(tfttouch.touched()) {
    TS_Point p = tfttouch.getPoint();
    Serial.print("Pressure = ");
    Serial.print(p.z);
    Serial.print(", x = ");
    Serial.print(p.x);
    Serial.print(", y = ");
    Serial.print(p.y);
    delay(30);
    Serial.println();
  }
}



unsigned long testFillScreen() {
  unsigned long start = micros();
  tftdisp.fillScreen(ILI9341_BLACK);
  yield();
  tftdisp.fillScreen(ILI9341_RED);
  yield();
  tftdisp.fillScreen(ILI9341_GREEN);
  yield();
  tftdisp.fillScreen(ILI9341_BLUE);
  yield();
  tftdisp.fillScreen(ILI9341_BLACK);
  yield();
  return micros() - start;
}

unsigned long testText() {
  tftdisp.fillScreen(ILI9341_BLACK);
  unsigned long start = micros();
  tftdisp.setCursor(0, 0);
  tftdisp.setTextColor(ILI9341_WHITE);  tftdisp.setTextSize(1);
  tftdisp.println("Hello World!");
  tftdisp.setTextColor(ILI9341_YELLOW); tftdisp.setTextSize(2);
  tftdisp.println(1234.56);
  tftdisp.setTextColor(ILI9341_RED);    tftdisp.setTextSize(3);
  tftdisp.println(0xDEADBEEF, HEX);
  tftdisp.println();
  tftdisp.setTextColor(ILI9341_GREEN);
  tftdisp.setTextSize(5);
  tftdisp.println("Groop");
  tftdisp.setTextSize(2);
  tftdisp.println("I implore thee,");
  tftdisp.setTextSize(1);
  tftdisp.println("my foonting turlingdromes.");
  tftdisp.println("And hooptiously drangle me");
  tftdisp.println("with crinkly bindlewurdles,");
  tftdisp.println("Or I will rend thee");
  tftdisp.println("in the gobberwarts");
  tftdisp.println("with my blurglecruncheon,");
  tftdisp.println("see if I don't!");
  return micros() - start;
}

unsigned long testLines(uint16_t color) {
  unsigned long start, t;
  int           x1, y1, x2, y2,
                w = tftdisp.width(),
                h = tftdisp.height();

  tftdisp.fillScreen(ILI9341_BLACK);
  yield();
  
  x1 = y1 = 0;
  y2    = h - 1;
  start = micros();
  for(x2=0; x2<w; x2+=6) tftdisp.drawLine(x1, y1, x2, y2, color);
  x2    = w - 1;
  for(y2=0; y2<h; y2+=6) tftdisp.drawLine(x1, y1, x2, y2, color);
  t     = micros() - start; // fillScreen doesn't count against timing

  yield();
  tftdisp.fillScreen(ILI9341_BLACK);
  yield();

  x1    = w - 1;
  y1    = 0;
  y2    = h - 1;
  start = micros();
  for(x2=0; x2<w; x2+=6) tftdisp.drawLine(x1, y1, x2, y2, color);
  x2    = 0;
  for(y2=0; y2<h; y2+=6) tftdisp.drawLine(x1, y1, x2, y2, color);
  t    += micros() - start;

  yield();
  tftdisp.fillScreen(ILI9341_BLACK);
  yield();

  x1    = 0;
  y1    = h - 1;
  y2    = 0;
  start = micros();
  for(x2=0; x2<w; x2+=6) tftdisp.drawLine(x1, y1, x2, y2, color);
  x2    = w - 1;
  for(y2=0; y2<h; y2+=6) tftdisp.drawLine(x1, y1, x2, y2, color);
  t    += micros() - start;

  yield();
  tftdisp.fillScreen(ILI9341_BLACK);
  yield();

  x1    = w - 1;
  y1    = h - 1;
  y2    = 0;
  start = micros();
  for(x2=0; x2<w; x2+=6) tftdisp.drawLine(x1, y1, x2, y2, color);
  x2    = 0;
  for(y2=0; y2<h; y2+=6) tftdisp.drawLine(x1, y1, x2, y2, color);

  yield();
  return micros() - start;
}

unsigned long testFastLines(uint16_t color1, uint16_t color2) {
  unsigned long start;
  int           x, y, w = tftdisp.width(), h = tftdisp.height();

  tftdisp.fillScreen(ILI9341_BLACK);
  start = micros();
  for(y=0; y<h; y+=5) tftdisp.drawFastHLine(0, y, w, color1);
  for(x=0; x<w; x+=5) tftdisp.drawFastVLine(x, 0, h, color2);

  return micros() - start;
}

unsigned long testRects(uint16_t color) {
  unsigned long start;
  int           n, i, i2,
                cx = tftdisp.width()  / 2,
                cy = tftdisp.height() / 2;

  tftdisp.fillScreen(ILI9341_BLACK);
  n     = min(tftdisp.width(), tftdisp.height());
  start = micros();
  for(i=2; i<n; i+=6) {
    i2 = i / 2;
    tftdisp.drawRect(cx-i2, cy-i2, i, i, color);
  }

  return micros() - start;
}

unsigned long testFilledRects(uint16_t color1, uint16_t color2) {
  unsigned long start, t = 0;
  int           n, i, i2,
                cx = tftdisp.width()  / 2 - 1,
                cy = tftdisp.height() / 2 - 1;

  tftdisp.fillScreen(ILI9341_BLACK);
  n = min(tftdisp.width(), tftdisp.height());
  for(i=n; i>0; i-=6) {
    i2    = i / 2;
    start = micros();
    tftdisp.fillRect(cx-i2, cy-i2, i, i, color1);
    t    += micros() - start;
    // Outlines are not included in timing results
    tftdisp.drawRect(cx-i2, cy-i2, i, i, color2);
    yield();
  }

  return t;
}

unsigned long testFilledCircles(uint8_t radius, uint16_t color) {
  unsigned long start;
  int x, y, w = tftdisp.width(), h = tftdisp.height(), r2 = radius * 2;

  tftdisp.fillScreen(ILI9341_BLACK);
  start = micros();
  for(x=radius; x<w; x+=r2) {
    for(y=radius; y<h; y+=r2) {
      tftdisp.fillCircle(x, y, radius, color);
    }
  }

  return micros() - start;
}

unsigned long testCircles(uint8_t radius, uint16_t color) {
  unsigned long start;
  int           x, y, r2 = radius * 2,
                w = tftdisp.width()  + radius,
                h = tftdisp.height() + radius;

  // Screen is not cleared for this one -- this is
  // intentional and does not affect the reported time.
  start = micros();
  for(x=0; x<w; x+=r2) {
    for(y=0; y<h; y+=r2) {
      tftdisp.drawCircle(x, y, radius, color);
    }
  }

  return micros() - start;
}

unsigned long testTriangles() {
  unsigned long start;
  int           n, i, cx = tftdisp.width()  / 2 - 1,
                      cy = tftdisp.height() / 2 - 1;

  tftdisp.fillScreen(ILI9341_BLACK);
  n     = min(cx, cy);
  start = micros();
  for(i=0; i<n; i+=5) {
    tftdisp.drawTriangle(
      cx    , cy - i, // peak
      cx - i, cy + i, // bottom left
      cx + i, cy + i, // bottom right
      tftdisp.color565(i, i, i));
  }

  return micros() - start;
}

unsigned long testFilledTriangles() {
  unsigned long start, t = 0;
  int           i, cx = tftdisp.width()  / 2 - 1,
                   cy = tftdisp.height() / 2 - 1;

  tftdisp.fillScreen(ILI9341_BLACK);
  start = micros();
  for(i=min(cx,cy); i>10; i-=5) {
    start = micros();
    tftdisp.fillTriangle(cx, cy - i, cx - i, cy + i, cx + i, cy + i,
      tftdisp.color565(0, i*10, i*10));
    t += micros() - start;
    tftdisp.drawTriangle(cx, cy - i, cx - i, cy + i, cx + i, cy + i,
      tftdisp.color565(i*10, i*10, 0));
    yield();
  }

  return t;
}

unsigned long testRoundRects() {
  unsigned long start;
  int           w, i, i2,
                cx = tftdisp.width()  / 2 - 1,
                cy = tftdisp.height() / 2 - 1;

  tftdisp.fillScreen(ILI9341_BLACK);
  w     = min(tftdisp.width(), tftdisp.height());
  start = micros();
  for(i=0; i<w; i+=6) {
    i2 = i / 2;
    tftdisp.drawRoundRect(cx-i2, cy-i2, i, i, i/8, tftdisp.color565(i, 0, 0));
  }

  return micros() - start;
}

unsigned long testFilledRoundRects() {
  unsigned long start;
  int           i, i2,
                cx = tftdisp.width()  / 2 - 1,
                cy = tftdisp.height() / 2 - 1;

  tftdisp.fillScreen(ILI9341_BLACK);
  start = micros();
  for(i=min(tftdisp.width(), tftdisp.height()); i>20; i-=6) {
    i2 = i / 2;
    tftdisp.fillRoundRect(cx-i2, cy-i2, i, i, i/8, tftdisp.color565(0, i, 0));
    yield();
  }

  return micros() - start;
}