/*
how to use threading, available since c++11

note, output:
starting
0: part1
0: part2
1: part1
1: part2
2: part1
2: part2
3: part1
4: part1
3: part2
4: part2
done

*/

#include <thread> // c++11 standard
#include <chrono> // only for test function
#include <string> // only for test function
uint64_t get_epoch_micros(){
    uint64_t tnow = std::chrono::time_point_cast<std::chrono::microseconds>(
        std::chrono::system_clock::now()).time_since_epoch().count();
    //std::cout << tnow << "\n";
    return tnow;
}

void sayNtimes(std::string statement,uint64_t delay_us) {
    uint64_t t_finish;
    for (int i = 0; i < 5; i++) {
        printf("%d: %s\n", i,statement.c_str());
        t_finish = get_epoch_micros() + delay_us;
        while (get_epoch_micros() < t_finish);
    }
}

// lambda expression may be easiest way to set thread (avoids passing arguments)
auto fn_t1 = []() { sayNtimes("part1", 1 * 1e6); };
//auto fn_t2 = []() { sayNtimes("part2", (uint64_t)(1.5 * 1e6)); };

int main(){
    printf("starting\n");
    std::thread th1(fn_t1);
    std::thread th2(sayNtimes,"part2", (uint64_t)(1.5 * 1e6));
    th1.join();
    th2.join();
    printf("done\n");
    return 0;
}




// eof
