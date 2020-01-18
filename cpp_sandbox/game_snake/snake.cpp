/*
date: 200118
objective: create the game snake, in cpp. for the moment, GUI will be in opencv. later may want to use Qt libraries

GENERAL ISSUES / OBJECTIVES
STAT | DESCRIPTION
???? | initialize basic libraries, keyboard control
???? | create game board (10x10 grid)
???? | create "snake" object as single block
???? | be able to move snake with WASD
???? | create "apple" object
???? | create "auto-move" behavior (snake is always moving)
???? | create "eating" behavior (head of snake occupies apple location)
???? | create "growing" behavior (snake length increases when eating an apple)

*/

#include <iostream>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <random>

