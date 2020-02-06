/*
date: 200206
objective: program snake in the stupidest way. really tired of dealing with the
    GUI / keyboard events crap. will just do it as a turn-based approach. this
    will help get things up and running by the time that wxwidgets can be used
    effectively. effectively, a text-based approach will be used.

sample board:
XXXXXXXXXXXX
X          X
X          X
X          X
X          X
XXXXXXXXXXXX



STAT | DESCRIPTION
done | board shown (use r-c coordinates, top-left origin)
done | show apple object
???? | board has random location generator
???? | show snake object
???? | eat apple
???? | randomly re-place apple
???? | increase snake length on eat
???? | ??
???? | ??
???? | ??

strange error happening with repeated runs of program with random function:
Exception: STATUS_ACCESS_VIOLATION at rip=003CC1CCBA1
rax=0000000000000000 rbx=0000000600085080 rcx=000000010040400B
rdx=0000000000000002 rsi=0000000600085080 rdi=000000018030ABD0
r8 =0000000000000001 r9 =000000010040400B r10=000000010040400B
r11=0000000600084D38 r12=0000000000000002 r13=00000000FFFFCC76
r14=0000000000000000 r15=00000000FFFFCC76
rbp=0000000000000001 rsp=00000000FFFFB6C0
program=C:\Users\kris\codefiles\cpp_sandbox\snake_stupid\a.exe, pid 1493, thread main
cs=0033 ds=002B es=002B fs=0053 gs=002B ss=002B




*/
#include <iostream>
#include <vector>
#include <random>
using namespace std;
class Apple{
    /* Class that tracks the r and c locations of the apple */
public:
    int r,c;
    Apple(int r_,int c_){r=r_;c=c_;}
};

class Snake{
    /* track location of snake head and body*/
public:
    int rHead, cHead;
    std::vector<int[2]> v;
    Snake(int r_, int c_){
        /* initialize snake position, and must take care not to put too close to
            wall, or facing walls
        */
        rHead=r_;cHead=c_;
    }

    void move(int direction){
        /* update snake head position and rest of body*/
    }
    void grow(){
        /* upon next move, extend body length by one.*/
    }
};

class Board{
    /* take in game elements, display them, check for collisions*/
public:
    int rSize,cSize; // usable dimensions
    std::vector<string> bb;

    Board(int rSize_=10,int cSize_=20){rSize=rSize_;cSize=cSize_;redrawBoard();}
    void print(){
        // show board's current state
        for(int i=0;i<bb.size();i++) printf("%s",bb[i].c_str());cout << endl;
    }
    void redrawBoard(){
        // redraw blank board
        bb.push_back( string(cSize+2,'X')+"\n" ); //top
        for(int i=0;i<rSize;i++){bb.push_back( "X" + string(cSize,' ')+"X\n");} //mid
        bb.push_back( string(cSize+2,'X') ); //bottom
    }//redrawBoard
    void drawApple(Apple &a){
        // draw apple coordinate on board, a single letter
        bb[a.r+1].replace(a.c+1,1,"A");
    }
    void drawSnake(Snake &s){
        // draw entire snake, starting with head.
        bb[s.rHead+1].replace(s.cHead+1,1,"O");
    }
};


int main(){
    int r=10; int c=20; // desired board dimensions
    random_device rand; // initialize random number generator

    Apple apple(8,8); // this is generating some kind of issue...?
    Snake snake(4,4);
    Board board(r,c);
    board.drawApple(apple);
    board.drawSnake(snake);
    board.print();
    return 0;

// aspect ratio: 2:1

    // // don't want this to run at the moment
    // int x;
    // cout << "give a number: ";
    // cin >> x;
    // cout << "you gave: " << x << endl;


}
