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

*/
#include <iostream>
#include <vector>
#include <cstdlib> // easiest way to have a random number
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
        for(int i=0;i<rSize-2;i++){bb.push_back( "X" + string(cSize,' ')+"X\n");} //mid
        bb.push_back( string(cSize+2,'X') ); //bottom
    }//redrawBoard
    void drawApple(int r,int c){
        // draw apple coordinate on board, a single letter
        bb[r+1].replace(c+1,1,"A");
    }
};


int main(){

    //alright, let's figure out how to make something random
    // attempt 1: use cstdlib & rand()%maxvalue
    // cout << rand()%20 << endl; // FAIL

    // attempt 2: try to incorporate time variable


    return 0;

    int r,c;
    r=10; // desired board dimensions
    c=20;
    Board board(r,c);
    board.drawApple(rand()%r,rand()%c);
    board.print();
    return 0;

// aspect ratio: 2:1

    // don't want this to run at the moment
    int x;
    cout << "give a number: ";
    cin >> x;
    cout << "you gave: " << x << endl;


}
