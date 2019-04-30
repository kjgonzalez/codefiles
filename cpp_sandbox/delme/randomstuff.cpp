/*
emulate what you saw in "evaluate_object_3d_offline.cpp" file
*/

#include <iostream>
#include <vector>
using namespace std;

enum CLASSES{CAR=3, PEDESTRIAN=4, CYCLIST=5};
const int NUM_CLASS = 3;

int main(){
    vector<bool> eval_image(NUM_CLASS,false);
    for(int i=0;i<eval_image.size();i++) cout<<eval_image[i]<< ' ';
    printf("\n");
    return 0;
}
