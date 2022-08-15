#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s;
        
        for(auto x: nums){
            s.insert(x);
        }
        int maxSequence = 0, size = 0;
        for(auto x: s){
            size = 1;
            // if it is not start of band then don't travserse it.
            if(s.find(x-1) != s.end()){
                continue;
            }
            int k = x +1; 
            while(s.find(k) != s.end()){
                k++;
                size++;
            }
            maxSequence = size > maxSequence ? size : maxSequence;
        }
        return maxSequence;    
    }
};