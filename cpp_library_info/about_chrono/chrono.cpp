/*
chrono library - high resolution clocks

notes: 
* steady_clock: like a stopwatch
* system_watch: like a wall clock. note: may periodically sync with an atomic clock thus may not 
    always be consistent with true differences in time

sources: 
* steady_clock vs system_clock: https://stackoverflow.com/questions/31552193/difference-between-steady-clock-vs-system-clock

*/

#include <chrono>
namespace ch = std::chrono; // can help shorten the long names

using time_stamp = std::chrono::time_point<std::chrono::system_clock, std::chrono::microseconds>;

uint64_t get_epoch_micros() {
    uint64_t tnow = std::chrono::time_point_cast<std::chrono::microseconds>(
        std::chrono::system_clock::now()).time_since_epoch().count();
    //std::cout << tnow << "\n";
    return tnow;
}

void get_time_difference() {
    // don't need to immediately get full-res int64 timestamp, can get difference in time

    long long micros_wait = (long long)1e6; // wait 1s
    // example of shortening of namespace
    ch::steady_clock::time_point          t0 = std::chrono::high_resolution_clock::now();
    std::chrono::steady_clock::time_point t1 = std::chrono::high_resolution_clock::now();
    printf("pause... ");
    while ((std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count() < micros_wait)) {
        t1 = std::chrono::high_resolution_clock::now();
    }
    printf("done\n");
}

void get_time_tuple() {
    /* get time_epoch in(seconds, microseconds) format rather than together */
    std::chrono::system_clock::time_point t1 = std::chrono::system_clock::now(); //8bytes of memory
    uint32_t t2 = std::chrono::time_point_cast<std::chrono::seconds>(t1).time_since_epoch().count();
    uint32_t t3 = std::chrono::time_point_cast<std::chrono::microseconds>(t1).time_since_epoch().count() % t2;

    uint32_t s1 = sizeof(t1); // 8bytes
    uint32_t s2 = sizeof(t2); // 4bytes
    uint32_t s3 = sizeof(t3); // 4bytes
    printf("seconds: %lu (%d bytes)\n", t2, s2);
    printf("seconds: %lu (%d bytes)\n", t3, s3);
}


int main() {
    printf("micros: %llu\n",get_epoch_micros());
    printf("delay...\n");

    get_time_tuple();

    get_time_difference();

    return 0;
}




// eof
