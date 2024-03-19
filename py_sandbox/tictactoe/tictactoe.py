'''
fucking around on a plane, try making tic-tac-toe game to play against
'''

e=' ' # empty slot

import random
import argparse
import numpy as np

def equal(val_list):
    i0=val_list[0]
    for i in val_list[1:]:
        if(i0 != i): return False
    return True

class Spot:
    def __init__(self,x,y):
        self.val=e
        self.x=x
        self.y=y
    @property
    def loc(self):
        return self.x,self.y

class PcPlayer:
    ''' single class to hold all behaviors for tictactoe ai 
    todo: implement random ai
    todo: implement basic ai
    todo: implement NN ai
    '''
    def __init__(self):
        # initialize all possible parameters for ai
        self.style=0 # 0=rand,1=basic
        
    def playturn(self,gstate):
        ''' 
        Based on chosen playstyle, play a turn of tictactoe
        INPUT:
          gamestate: np array
        '''
        if(self.style==0): return self.styleRand(gstate)
        else: 
            raise Exception("invalid ai style given")
    def styleRand(self,gstate):
        # playstyle: place ranodm tiles
        done=False
        while(not done):
            r,c=random.randint(0,2),random.randint(0,2)
            if(gstate[r][c]==e):
                return (r,c)
                # self.boardstate[r][c]='O'
                done=True
        # pcplay_rand end
    def styleBasic(self,gstate):
        # simple ai, tries to look ahead and make good decisions
        ''' 
        Check board state and pick best place to play:
          0: collect all possible win conditions
          1: if will win, play that
          2: if other will win, block that
          3: if middle open, play that
          4: play somewhere random
        '''
        if(gstate[1][1]==e): return 1,1
        else: return self.styleRand(gstate)
        # pcplay_basic

class GameTicTacToe:
    def __init__(self):
        self.boardstate=np.array([[e,e,e],[e,e,e],[e,e,e]])
        self.move = ''
        self.turn=0 # 0=pc,1=player
        self.ai = PcPlayer()
    def print(self):
        ''' print boardstate '''
        for irow in self.boardstate: print('|'.join(irow))
    @staticmethod
    def invalid():
        print('invalid input')
        return 0
    @property
    def board1d(self):
        return [i for irow in self.boardstate for i in irow]
    @property
    def board8d(self):
        ''' return all vectors to check for win condition (8 options) '''
        k = self.board1d
        v = []
        v.append([k[0],k[1],k[2]]) # top
        v.append([k[3],k[4],k[5]]) # mid
        v.append([k[6],k[7],k[8]]) # bot

        v.append([k[0],k[3],k[6]]) # lhs
        v.append([k[1],k[4],k[7]]) # mid
        v.append([k[2],k[5],k[8]]) # rhs
        
        v.append([k[0],k[4],k[8]]) # bslash
        v.append([k[2],k[4],k[6]]) # fslash
        return v
    def playround(self):
        ''' 
        play next round of game
        1. get player input (as "row,col") coordinates
        2. check if player won
        3. if not, computer makes next move
        4. update board state
        5. if player won, exit loop
        '''
        if(self.turn):
            print('player turn ("X")')
            self.print()
            move = input('move ("r,c" 0-index, or q to quit): ')
            if(move=='q'): return 1 # exit
            if(move.isalpha()): return self.invalid()
            try: r,c = [int(i) for i in move.split(',')]
            except: return self.invalid()
            if(r not in [0,1,2] or c not in [0,1,2]): return self.invalid()
            if(self.boardstate[r][c]!=e):
                print('invalid location')
                return 0
            self.boardstate[r][c]='X'
            self.turn=0 # set to pc turn
        else:
            print('pc turn ("O")')
            loc=self.ai.playturn(self.boardstate)
            self.boardstate[loc[0]][loc[1]] = 'O'
            self.turn=1 #set to player turn
        # check if anyone won
        res = self.checkwin()
        return res
    def checkwin(self):
        ''' Look at boardstate for win / end condition '''
        # check if anyone won (8 ways)
        for ivec in self.board8d:
            if(equal(ivec)):
                if(  ivec[0]=='O'): return 3
                elif(ivec[0]=='X'): return 4

        # if no one won, check if board is full (draw)
        nEmpty=0
        for ir in range(3):
            for ic in range(3):
                if(self.boardstate[ir][ic]==e):nEmpty+=1
        if(nEmpty==0): return 2
        else: return 0

    def run(self):
        ''' 
        Run one game until end condition reached.
        res values:
        0 = not done
        1 = quit
        2 = draw
        3 = pc win
        4 = player win
        '''
        # initialize new game
        self.boardstate=np.array([[e,e,e],[e,e,e],[e,e,e]])
        self.turn = random.randint(0,1)
        res = 0
        while(not res):
            res = self.playround()
        self.print()
        string = '. quit tie pcWin playerWin'.split(' ')
        print('game end:',string[res])
    def runmultiple(self):
        v = ''
        while(v!='q'):
            self.run()
            v = input("q again to exit, ENTER to restart: ")

if(__name__ == '__main__'):
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--loop',default=False,action='store_true',help="auto-restart")
    args = p.parse_args()

    g = GameTicTacToe()
    if(args.loop): g.runmultiple()
    else: g.run()
    print('end of program')




