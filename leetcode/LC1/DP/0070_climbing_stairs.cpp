#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <unordered_map>
using namespace std;

// fibonacci series
class Solution {
public:
    int climbStairs(int n) {
        if(n == 0 || n == 1 || n == 2)return n;
        int secondLast = 1;
        int Last = 2;
        int totalSteps = 0;
        for(int i= 3; i <= n; i++){
            totalSteps = Last + secondLast;
            secondLast = Last;
            Last = totalSteps;
        }
        return totalSteps;
    }
};
