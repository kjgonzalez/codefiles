#include <iostream>
#include <map>
using std::cout;
using std::endl;

int main()
{
    //basic way of declaring / assigning a map
    std::map<int,float> m1;
    for(int i=0;i<4;i++){ m1[i] = (float)i*1.1; }

    // declare everything at once
    std::map<int, float> m2 = {{1,2.2}, {2,2.2}, {3,3.4}};

    typedef std::map<int,float> mymap_t; // sometimes, easier to just define map & item type
    typedef mymap_t::iterator mymapit_t;
    mymap_t m3;
    m3[0]=-1.1;
    m3[1]=2.1;

    cout << "size: " << m1.size() << endl;
    mymap_t::iterator ipair1 = m1.find(2);
    cout << "find(2): " << ipair1->second << endl;
    //cout << "find(-1): " << ipair2->first << " " << ipair2->second << endl; // would fail
    mymapit_t ipair2 = m1.find(-1);
    bool wasfound = ipair2 != m1.end(); // if(ipair==end()), then KEY WAS NOT FOUND
    cout << "was key [" << -1 << "] found? " << wasfound << endl;
    cout << "m1[1]: " << m1[1] << endl;
    cout << "m1[2]: " << m1.at(2) << endl; // safer, throws error if element doesn't exist
    m1.erase(1); // drop an element
    m1.clear(); // remove all elements
    m1[1] = 1.1;
    m1.insert({2,2.2});
    m1.insert({2,3.3}); // won't be kept, key already inside
    cout << "which was kept: " << m1[2] << endl;
    m1[2] = 4.4; // this WILL overwrite previous value, because not creation, but modification
    cout << "kept part 2: " << m1[2] << endl;

    // another way to check if something exists, "count"
    cout << "has 10: " << m1.count(10) << endl;

    printf("---\n");
    for(auto item : m2){ printf("m2[%d]: %f\n",item.first,item.second); }

    return 0;
}