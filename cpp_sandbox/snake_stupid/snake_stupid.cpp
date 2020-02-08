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

aspect ratio: 2:1


STAT | DESCRIPTION
done | board shown (use r-c coordinates, top-left origin)
done | show apple object
done | board has random location generator
done | show snake object
done | move snake
???? | eat apple
???? | randomly re-place apple
???? | increase snake length on eat
???? | detect when snake hits a wall
???? | detect when snake eats apple
???? | detect when snake hits itself
???? | disable snake moving into itself (instant-uTurn)
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
    int rHead, cHead,dir;
    vector<vector<int>> v;
    Snake(int r_, int c_,int dir_=0){
        /* initialize snake position, and must take care not to put too close to
            wall, or facing walls
            direction: 0=up,1=right,2=down,3=left (snake goes that direction initially)
            1. get head position & direction
            2. setup body position
        */
        rHead=r_;cHead=c_;dir=dir_;
        v.push_back({r_,c_});
        if(dir_==0){
            v.push_back({r_+1,c_});
            v.push_back({r_+2,c_});
        }
        else if(dir_==1){
            v.push_back({r_,c_-1});
            v.push_back({r_,c_-2});
        }
        else if(dir_==2){
            v.push_back({r_-1,c_});
            v.push_back({r_-2,c_});
        }

        else if(dir_==3){
            v.push_back({r_,c_+1});
            v.push_back({r_,c_+2});
        }
        else{
            printf("ERROR, MAY THROW ERROR\n");
        }



    }
    void printLoc(){
        // print out current location of each body part
        for(int i=0;i<v.size();i++){
            printf("%i: (%i,%i)\n",i,v[i][0],v[i][1]);
        }
    }
    void move(int dir){
        /* update snake head position and rest of body*/

        // first, check that not doing insta-uTurn
        int r_=v[0][0];
        int c_=v[0][1];
        vector<int> newHead;
        if(dir==0){newHead={r_-1,c_};} // up
        else if(dir==1){newHead={r_,c_+1};}
        else if(dir==2){newHead={r_+1,c_};}
        else if(dir==3){newHead={r_,c_-1};}
        else{
            printf("ERROR, MAY THROW ERROR HERE\n");
        }
        if(newHead[0]==v[1][0] && newHead[1]==v[1][1]){
            printf("direction not allowed\n");
        }
        else{
            // allowable direction
            // move snake in one direction. update tail-to-head
            for(int i=v.size()-1;i>0;i--){
                v[i]=v[i-1];
            }
            // update head
            // 1,2,3,4=up,right,down,left
            v[0][0]=newHead[0];
            v[0][1]=newHead[1];
        }//if newHead not in bad position
    }//void move

    void grow(){
        /* upon next move, extend body length by one.*/
    }
};

class Board{
    /* take in game elements, display them, check for collisions*/
public:
    int rSize,cSize; // usable dimensions
    vector<string> bb;
    Apple *pApple;
    Snake *pSnake;

    Board(Apple &a,Snake &s,int rSize_=10,int cSize_=20){
        pApple=&a;
        pSnake=&s;
        rSize=rSize_;cSize=cSize_;
        // initialize board
        bb.push_back( string(cSize+2,'X')+"\n" ); //top
        for(int i=0;i<rSize;i++){bb.push_back( "X" + string(cSize,' ')+"X\n");} //mid
        bb.push_back( string(cSize+2,'X')+"\n" ); //bottom
    }
    void print(){
        // show board's current state
        for(int i=0;i<bb.size();i++) printf("%s",bb[i].c_str());cout << endl;
    }
    void redrawBoard(){
        // redraw blank board
        for(int i=1;i<rSize+1;i++){
            for(int j=1;j<cSize+1;j++){
                bb[i].replace(j,1," ");
            }
        }
    }//redrawBoard
    void drawApple(){
        // draw apple coordinate on board, a single letter
        bb[pApple->r+1].replace(pApple->c+1,1,"A");
    }
    void drawSnake(){
        // draw entire snake, starting with head.
        for(int i=0;i<pSnake->v.size();i++){
            if(i==0)bb[pSnake->v[i][0]].replace(pSnake->v[i][1],1,"0"); //head
            else bb[pSnake->v[i][0]].replace(pSnake->v[i][1],1,"o");
        }//forloop
    } // drawSnake
    void updatePrint(){
        redrawBoard();
        drawApple();
        drawSnake();
        print();
    }
};


int main(){
    int r=10; int c=20; // desired board dimensions
    random_device rand; // initialize random number generator
    Apple apple(8,8); // this is generating some kind of issue...?
    Snake snake(4,7,0);
    Board board(apple,snake,r,c);
    // board.updatePrint();
    char dir='w';
    int dir_=0;
    while(dir!='q'){
        board.updatePrint();
        cout << "please give a direction ('q' to quit): ";
        cin >> dir;
        switch(dir){
            case('w'):dir_=0;break;
            case('a'):dir_=3;break;
            case('s'):dir_=2;break;
            case('d'):dir_=1;break;
            default:dir_=0;break;
        }//case(dir)
        snake.move(dir_);
    }//whileloop
    return 0;
}
