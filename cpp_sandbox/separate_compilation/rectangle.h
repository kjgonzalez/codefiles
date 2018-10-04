/*
here, we're using a "simple" approach to include code from the main cpp program
  in another location (to create modularity / simplicity). however, it's
  recommended by stroustrup (cpp_language,p425) to avoid including functions in
  a header file
*/

class rect{
public:
  int ht,wd;
    rect(int height,int width){
      ht=height;
      wd=width;
    }//constructor
    int area(){
      return ht*wd;
    }//void area
    int perim(){
      return 2*(ht+wd);
    }//void perim
}; //class rect
