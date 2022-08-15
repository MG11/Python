
// //https://leetcode.com/problems/logger-rate-limiter/discuss/365306/Simple-Two-HashMap-Solution-with-O(1)-time-and-little-memory/640609
#include <unordered_map>
#include <string>
using namespace std;

class Logger {
public:
    unordered_map <string, int> prev;
    unordered_map <string, int> curr;
    int init_time;
    Logger() {    
        init_time = 0;
    }
    
    bool shouldPrintMessage(int timestamp, string message) {
        if(timestamp >= init_time + 10){
            prev = curr;
            curr.clear();
            init_time = timestamp;
        }
        
        if(curr.find(message) != curr.end())
           return false;
        if(prev.find(message) != prev.end() && prev[message] + 10 > timestamp)
           return false;
        curr[message] = timestamp;
        return true;
    }
};
