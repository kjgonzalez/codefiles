/*
basic intro to cpp filesystem library. showing items below with reference to python os.path module
*/
#include <iostream>
#include <filesystem>

int main()
{
    using std::cout;
    using std::endl;
    printf("about: filesystem (note: requires C++17)\n");

    std::filesystem::create_directory("testhere");
    cout << "is 'testhere/' a directory? " << std::filesystem::is_directory("testhere") << endl;
    cout << "is 'out.exe' a file? " << std::filesystem::is_regular_file("out.exe") << endl;
    cout << "list of file in current directory: \n";

    std::filesystem::path myfile;
    for (auto item : std::filesystem::directory_iterator(".")) {
        cout << "  " << item.path() << endl;
        if (myfile.empty() && item.is_regular_file() && item.path().filename().c_str()[0] !='.')
            // don't want a file that has no basename (e.g. .gitignore)
            myfile = std::filesystem::absolute(item);
    }

    cout << "absolute path to some file: " << myfile << endl;
    cout << "parent directory: " << myfile.parent_path() << endl;
    cout << "extension of file: " << myfile.extension() << endl;
    cout << "basename ('stem'):" << myfile.stem() << endl;

    return 0;
}