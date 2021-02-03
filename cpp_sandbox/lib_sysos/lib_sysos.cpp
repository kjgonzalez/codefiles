/*

try and cover the type of operations that are used in python modules "os" and "sys"

MAJOR NOTE: focus on making this work in windows first, then in linux
os: 
    name (name of os)
    chdir
    getlogin ? 
    getpid ? 
    mkdir
    makedirs (recursive)
    remove (file-only)
    want: copy

    path:
        abspath
        basename ("/foo/bar/" -> "bar")
        dirname ("/foo/bar/" -> "/foo")
        exists (whether file / folder exists
        getsize
        isdir
        isfile
        join
        split
        sep (either '/' or '\\'
*/

#include <iostream>
#include <filesystem>
using namespace std;
namespace fs = std::filesystem;

int main(int argc, char **argv) {
    // std::printf("where: %s\n", argv[0]);
    fs::path p = argv[0];
    std::cout << fs::current_path() << "\n";



}





// eof
