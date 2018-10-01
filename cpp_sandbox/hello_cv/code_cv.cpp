#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;

/*
KJG180305: this code works, along with CMakeList.txt file
in order to compile the code: 
1. write all code
2. create CMakeLists.txt file
3. run commands:
	cd <TheDirectoryLocation>
	cmake .
	make
*/

int main(int argc, char** argv )
{
    if ( argc != 2 )
    {
        printf("usage: DisplayImage.out <Image_Path>\n");
        return -1;
    }

    Mat image;
    image = imread( argv[1], 1 );

    if ( !image.data )
    {
        printf("No image data \n");
        return -1;
    }
    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", image);

    waitKey(0);

    return 0;
}