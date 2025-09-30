#include <Arduino.h>
#define dw digitalWrite

static const int pe=7;
static const int pd=8;
static const int pp=9;
static const int pc=10;
static const int pg=11;
static const int p4=12;
static const int pb=13;
static const int p3=14;
static const int p2=15;
static const int pf=16;
static const int pa=17;
static const int p1=18;

class SevenSegmentX4
{
    int _pa,_pb,_pc,_pd,_pe,_pf,_pg,_pp,_p0,_p1,_p2,_p3;
    bool is_setup=false;
    char buf[100];
    char bufdraw[4];
    int drawind=4;
    float myval;
    IntervalTimer myt;


    // select which digit to print out (0-3)
    void setd(int d){ dw(_p0,0!=d); dw(_p1,1!=d); dw(_p2,2!=d); dw(_p3,3!=d); }

    void drawDot(bool val) { dw(_pp,val); }

    public:
    SevenSegmentX4()
    {
        is_setup=false;
        for(int i=0;i<100;i++) buf[i]=0;
        for(int i=0;i<4;i++) bufdraw[i]=0;
    }
    void init(int PA, int PB, int PC, int PD, int PE, int PF, int PG, int PP, int P0, int P1, int P2, int P3)
    {
        is_setup=true;
        _pa=PA; _pb=PB; _pc=PC; _pd=PD; _pe=PE; _pf=PF; _pg=PG; _pp=PP; _p0=P0; _p1=P1; _p2=P2; _p3=P3;
        pinMode(_pa,1); pinMode(_pb,1); pinMode(_pc,1); pinMode(_pd,1); pinMode(_pe,1); pinMode(_pf,1);
        pinMode(_pg,1); pinMode(_pp,1); pinMode(_p0,1); pinMode(_p1,1); pinMode(_p2,1); pinMode(_p3,1);
        this->_drawReset();
    }

    void _drawReset() { dw(_pa,0); dw(_pb,0); dw(_pc,0); dw(_pd,0); dw(_pe,0); dw(_pf,0); dw(_pg,0); dw(_pp,0); setd(0); }
    void _drawNull(int d) { dw(_pa,0); dw(_pb,0); dw(_pc,0); dw(_pd,0); dw(_pe,0); dw(_pf,0); dw(_pg,0); drawDot(false); setd(d); }
    void _draw0(int d,bool dot=false) { dw(_pa,1); dw(_pb,1); dw(_pc,1); dw(_pd,1); dw(_pe,1); dw(_pf,1); dw(_pg,0); drawDot(dot); setd(d); }
    void _draw1(int d,bool dot=false) { dw(_pa,0); dw(_pb,1); dw(_pc,1); dw(_pd,0); dw(_pe,0); dw(_pf,0); dw(_pg,0); drawDot(dot); setd(d); }
    void _draw2(int d,bool dot=false) { dw(_pa,1); dw(_pb,1); dw(_pc,0); dw(_pd,1); dw(_pe,1); dw(_pf,0); dw(_pg,1); drawDot(dot); setd(d); }
    void _draw3(int d,bool dot=false) { dw(_pa,1); dw(_pb,1); dw(_pc,1); dw(_pd,1); dw(_pe,0); dw(_pf,0); dw(_pg,1); drawDot(dot); setd(d); }
    void _draw4(int d,bool dot=false) { dw(_pa,0); dw(_pb,1); dw(_pc,1); dw(_pd,0); dw(_pe,0); dw(_pf,1); dw(_pg,1); drawDot(dot); setd(d); }
    void _draw5(int d,bool dot=false) { dw(_pa,1); dw(_pb,0); dw(_pc,1); dw(_pd,1); dw(_pe,0); dw(_pf,1); dw(_pg,1); drawDot(dot); setd(d); }
    void _draw6(int d,bool dot=false) { dw(_pa,1); dw(_pb,0); dw(_pc,1); dw(_pd,1); dw(_pe,1); dw(_pf,1); dw(_pg,1); drawDot(dot); setd(d); }
    void _draw7(int d,bool dot=false) { dw(_pa,1); dw(_pb,1); dw(_pc,1); dw(_pd,0); dw(_pe,0); dw(_pf,0); dw(_pg,0); drawDot(dot); setd(d); }
    void _draw8(int d,bool dot=false) { dw(_pa,1); dw(_pb,1); dw(_pc,1); dw(_pd,1); dw(_pe,1); dw(_pf,1); dw(_pg,1); drawDot(dot); setd(d); }
    void _draw9(int d,bool dot=false) { dw(_pa,1); dw(_pb,1); dw(_pc,1); dw(_pd,0); dw(_pe,0); dw(_pf,1); dw(_pg,1); drawDot(dot); setd(d); }
    void _drawa(int d,bool dot=false) { dw(_pa,1); dw(_pb,1); dw(_pc,1); dw(_pd,0); dw(_pe,1); dw(_pf,1); dw(_pg,1); drawDot(dot); setd(d); }
    void _drawb(int d,bool dot=false) { dw(_pa,0); dw(_pb,0); dw(_pc,1); dw(_pd,1); dw(_pe,1); dw(_pf,1); dw(_pg,1); drawDot(dot); setd(d); }
    void _drawc(int d,bool dot=false) { dw(_pa,0); dw(_pb,0); dw(_pc,0); dw(_pd,1); dw(_pe,1); dw(_pf,0); dw(_pg,1); drawDot(dot); setd(d); }
    void _drawd(int d,bool dot=false) { dw(_pa,0); dw(_pb,1); dw(_pc,1); dw(_pd,1); dw(_pe,1); dw(_pf,0); dw(_pg,1); drawDot(dot); setd(d); }
    void _drawe(int d,bool dot=false) { dw(_pa,1); dw(_pb,0); dw(_pc,0); dw(_pd,1); dw(_pe,1); dw(_pf,1); dw(_pg,1); drawDot(dot); setd(d); }
    void _drawf(int d,bool dot=false) { dw(_pa,1); dw(_pb,0); dw(_pc,0); dw(_pd,0); dw(_pe,1); dw(_pf,1); dw(_pg,1); drawDot(dot); setd(d); }
    void _drawg(int d,bool dot=false) { dw(_pa,1); dw(_pb,0); dw(_pc,1); dw(_pd,1); dw(_pe,1); dw(_pf,1); dw(_pg,0); drawDot(dot); setd(d); }
    void _drawh(int d,bool dot=false) { dw(_pa,0); dw(_pb,0); dw(_pc,1); dw(_pd,0); dw(_pe,1); dw(_pf,1); dw(_pg,1); drawDot(dot); setd(d); }
    void _drawi(int d,bool dot=false) { dw(_pa,0); dw(_pb,0); dw(_pc,1); dw(_pd,0); dw(_pe,0); dw(_pf,0); dw(_pg,0); drawDot(dot); setd(d); }
    void _drawj(int d,bool dot=false) { dw(_pa,0); dw(_pb,0); dw(_pc,1); dw(_pd,1); dw(_pe,0); dw(_pf,0); dw(_pg,0); drawDot(dot); setd(d); }
    void _drawl(int d,bool dot=false) { dw(_pa,0); dw(_pb,0); dw(_pc,0); dw(_pd,1); dw(_pe,1); dw(_pf,1); dw(_pg,0); drawDot(dot); setd(d); }
    void _drawn(int d,bool dot=false) { dw(_pa,0); dw(_pb,0); dw(_pc,1); dw(_pd,0); dw(_pe,1); dw(_pf,0); dw(_pg,1); drawDot(dot); setd(d); }
    void _drawo(int d,bool dot=false) { dw(_pa,0); dw(_pb,0); dw(_pc,1); dw(_pd,1); dw(_pe,1); dw(_pf,0); dw(_pg,1); drawDot(dot); setd(d); }
    void _drawp(int d,bool dot=false) { dw(_pa,1); dw(_pb,1); dw(_pc,0); dw(_pd,0); dw(_pe,1); dw(_pf,1); dw(_pg,1); drawDot(dot); setd(d); }
    void _drawu(int d,bool dot=false) { dw(_pa,0); dw(_pb,0); dw(_pc,1); dw(_pd,1); dw(_pe,1); dw(_pf,0); dw(_pg,0); drawDot(dot); setd(d); }
    void _drawy(int d,bool dot=false) { dw(_pa,0); dw(_pb,1); dw(_pc,1); dw(_pd,1); dw(_pe,0); dw(_pf,1); dw(_pg,1); drawDot(dot); setd(d); }
    void _drawDash(int d) { dw(_pa,0); dw(_pb,0); dw(_pc,0); dw(_pd,0); dw(_pe,0); dw(_pf,0); dw(_pg,1); drawDot(false); setd(d); }
    void _drawUscore(int d) { dw(_pa,0); dw(_pb,0); dw(_pc,0); dw(_pd,1); dw(_pe,0); dw(_pf,0); dw(_pg,0); drawDot(false); setd(d); }

    // print integer number (float later)
    void printNum(int val){
        //set internal buf
        for(int i=0;i<100;i++) buf[i]=0;
        sprintf(buf,"%d",val);
        bufdraw[0]=buf[0];
        bufdraw[1]=buf[1];
        bufdraw[2]=buf[2];
        bufdraw[3]=buf[3];
    }//fn

    void printText(char* cstr)
    {
        int i=0;
        while(cstr[i]!=0 && i<4){
            bufdraw[i]=cstr[i];
            i++;
        }
    }




    // update with timer interrupts
    void timerUpdate()
    {
        drawind = (drawind)%4+1;

        switch(bufdraw[drawind-1]){
            case('0'): {_draw0(drawind);break;}
            case('1'): {_draw1(drawind);break;}
            case('2'): {_draw2(drawind);break;}
            case('3'): {_draw3(drawind);break;}
            case('4'): {_draw4(drawind);break;}
            case('5'): {_draw5(drawind);break;}
            case('6'): {_draw6(drawind);break;}
            case('7'): {_draw7(drawind);break;}
            case('8'): {_draw8(drawind);break;}
            case('9'): {_draw9(drawind);break;}
            default:{_drawUscore(drawind);break;}
        }
    }

};


const int ledPin = LED_BUILTIN;  // the pin with a LED
bool ledState=false;
volatile unsigned long blinkCount = 0; // use volatile for shared variables
int mycount=0;

SevenSegmentX4 seg;
IntervalTimer myTimer;
void cbSegUpdate() { seg.timerUpdate(); }


void setup() {
    pinMode(ledPin, OUTPUT);
    seg.init(pa,pb,pc,pd,pe,pf,pg,pp,p1,p2,p3,p4);
    myTimer.begin(cbSegUpdate, 1000);  // blinkLED to run every 0.15 seconds

    seg.printText("hi");
    //seg.printNum(12);
}


void loop() {
    // delay(500);
    // mycount++;
    // seg.printNum(mycount);
}