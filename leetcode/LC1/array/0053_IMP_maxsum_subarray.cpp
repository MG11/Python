#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

// https://leetcode.com/problems/maximum-product-subarray/solution/
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currSum = 0;
        int maxSum = INT_MIN;
        int maximum = nums[0];
        for(int i = 0; i< nums.size(); i++){
            if (nums[i] > maximum)
            maximum = nums[i];
            currSum += nums[i];
            
            if(currSum > maxSum){
                maxSum = currSum;
            }
            
            if(currSum < 0){
                currSum = 0;
            }
        }
        
        if(maxSum < 0){
            maxSum = maximum;
        }
        return maxSum;
    }
};
