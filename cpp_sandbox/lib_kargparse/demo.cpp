/*

*/

#include <iostream>
#include "kargparse.hpp"

int main(int argc, char** argv)
{
    KArgParser _ap;
    _ap.add_desc("example usage of kargparser");
    _ap.add_req("pathname","path to file",atype_str);
    _ap.add_opt<uint64_t>("counterinit","initial count",4);
    _ap.add_flag("cuda","use cuda",false);
    _ap.parse(argc,argv);


    printf("hello world\n");
    printf("n args: %d\n",argc);
    return 0;
}





// eof

