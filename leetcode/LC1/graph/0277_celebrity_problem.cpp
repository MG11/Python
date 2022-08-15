#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <unordered_map>
using namespace std;

/* The knows API is defined for you.
      bool knows(int a, int b); */

class Solution {
    // knows api is given in question
    bool knows(int i, int j){
        return true;
    }
public:
    // knows(a, b) is true A cannot be celebrity else B cannot be celebrity
    int findCelebrity(int n) {
        int possible = 0, i = 0;
        // check if celebrity knows no one
        for(i = 0; i < n; i++){
            if(knows(possible, i)){
                // if possible knows i then possible can't be celebrity
                possible = i;
            }   
        }
        // only possible can be celebrity and no one else
        // check if everyone knows celebrity, and celebrity knows no one
        for(int i = 0; i< n; i++){
            if(i == possible)continue;
            if(!knows(i, possible) || knows(possible, i))
                return -1;
        }
     return possible;   
    }
};
