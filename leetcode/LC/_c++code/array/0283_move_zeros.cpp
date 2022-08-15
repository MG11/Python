/* 
take position of last non zero element to be inserted.
and insert non zero elements..

after that fill rest of the part with 0 elements..

*/

#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int lastNonZeroFountAt = 0;
        
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] != 0){
                nums[lastNonZeroFountAt++] = nums[i];
            }
        }   
        for(int i = lastNonZeroFountAt; i < nums.size() ; i++){
            nums[i] = 0;
        }
        
    }
};