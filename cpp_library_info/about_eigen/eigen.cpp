#include <iostream>
#include <Eigen/Dense>

int main()
{
    using std::cout;
    using std::endl;
    printf("hi\n");

    Eigen::Matrix4d mat = Eigen::Matrix4d::Identity();

    cout << "Identity:" << endl << mat << endl;




    return 0;
}