/*
how to use Eigen library a little bit like Numpy library. Keep in mind that there's some 
  functionality that doesn't exist in Eigen

Great external resource: https://gist.github.com/gocarlos/c91237b02c120c6319612e42fa196d77
*/

#include <iostream>
#include <vector>
#include <Eigen/Dense>
#include <Eigen/Eigenvalues> // needed for eigenvalue/vector operations
typedef Eigen::MatrixXd matxx; // convenience


Eigen::Vector2i eigShape(Eigen::MatrixXd& mat)
{
    Eigen::Vector2i s(mat.rows(), mat.cols());
    return s;
}

double eigStdDevCol(Eigen::MatrixX3d &mat, int colnum)
{
    double avg = mat.col(colnum).mean();
    double s = 0;
    for (int i = 0; i < mat.rows(); i++) { s += std::pow(mat(i, colnum) - avg, 2); }
    return std::pow(s / (mat.rows()), 0.5);
}

Eigen::MatrixXd eigCovariance(Eigen::MatrixXd mat)
{
    //matrix covariance has to be manually calculated. transpose in order to imitate np.cov behavior
    // todo: simplify instead of passing in copy & using transpose()
    matxx centered = mat.transpose().rowwise() - mat.transpose().colwise().mean();
    // note about above: result of operation is a vector, but individual terms are not typical vectors
    matxx cov = centered.adjoint() * centered / double(centered.rows() - 1);
    return cov;
}


int main()
{
    using std::cout;
    using std::endl;
    //typedef Eigen::MatrixXd matxx; // convenience



    printf("- basics ---\n"); // ================================================
    // load a matrix from text (e.g. requires dynamic matrix). here, will do intermediate step and provide a vector of vectors
    std::vector<Eigen::Vector3d> raw;
    float t = 0;
    for (int i = 0; i < 21; i++) { t = (float)i * 0.1; raw.push_back(Eigen::Vector3d(t, std::powf(t, 2), t * 3 - 2)); }

    // using X3 because the more assumptions Eigen can make about the data, the better. could also just use MatrixXd. Xf is dynamic, f
    Eigen::MatrixX3d arr1(raw.size(), 3);
    for (int i = 0; i < raw.size(); i++) { arr1.row(i) = raw[i]; }
    // note, ugly basic approach: arr1(i, 0) = raw[i].x();arr1(i, 1) = raw[i].y(); arr1(i, 2) = raw[i].z();

    Eigen::Matrix4d mat = Eigen::Matrix4d::Identity(); // fixed size, dynamic info
    cout << "Identity:" << endl << mat << endl;
    cout << "arr1 shape: \n" << eigShape((Eigen::MatrixXd)arr1) << endl;
    cout << "arr1.T shape: \n" << eigShape((Eigen::MatrixXd)arr1.transpose()) << endl;

    printf("- basic stats ---\n"); // ===========================================
    printf("shape: (%llu, %llu)\n", arr1.rows(), arr1.cols());
    cout << arr1 << endl;
    // get simple stats for all columns
    printf("min: "); for (int i = 0; i < arr1.cols(); i++) printf("%0.4f  ", arr1.col(i).minCoeff()); printf("\n");
    printf("max: "); for (int i = 0; i < arr1.cols(); i++) printf("%0.4f  ", arr1.col(i).maxCoeff()); printf("\n");
    printf("avg: "); for (int i = 0; i < arr1.cols(); i++) printf("%0.4f  ", arr1.col(i).mean()); printf("\n");
    printf("max: "); for (int i = 0; i < arr1.cols(); i++) printf("%0.4f  ", eigStdDevCol(arr1,i)); printf("\n");

    // slightly more advanced stats
    // np.cov(arr1.T) = 
    //   [[0.385, 0.770, 1.155]
    //    [0.770, 1.652, 2.310]
    //    [1.155, 2.310, 3.465]]
    
    cout << "cov(arr1.T):\n" << eigCovariance((matxx)arr1.transpose()) << endl;


    printf("- Norms ---\n"); // =================================================
    Eigen::Vector3d norm1(3, 4, 12);
    printf("norm(<3,4,12>) = %0.4f\n", norm1.norm());
    Eigen::MatrixX3d norm2(2,3);
    norm2.fill(0); // note: one way to initialize easily
    norm2 << 1, 2, 3, 4, 5, 6; // norm approx equal to 9.539
    printf("norm([[1,2,3],[4,5,6]]) = %0.4f\n", norm2.norm());

    printf("- Eigenvalues/vectors ---\n"); // ===================================
    /*
    np.linalg.eig(np.array([[2,1],[0,3]])) gives:
      eigvals={2,3}, 
      eigvecs={[1, sqrt(2)/2],[0, sqrt(2)/2]}
    */
    Eigen::Matrix2d eig1;
    eig1 << 2, 1, 0, 3;
    cout << "given: \n" << eig1 << endl;
    Eigen::EigenSolver<Eigen::Matrix2d> eigsolve(eig1);
    cout << "eigenvals: \n" << eigsolve.eigenvalues() << endl;
    cout << "eigenvectors: \n" << eigsolve.eigenvectors() << endl;
    cout << "**NOTE: returned as complex-comptible numbers/vectors..." << endl;




    //for (int i = 0; i < raw.size(); i++) {
    //    
    //}



    return 0;
}