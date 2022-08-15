#include <climits>
#include <iostream>
#include <vector>
#include <stack>
#include <unordered_set>
using namespace std;

// // https://www.youtube.com/watch?v=UmMh7xp07kY&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=8

class Solution {
public:
    bool canPartition(vector<int>& nums, const int &target){
        vector <int> arr(target+1, 0);
        arr[0] = 1;
        for(int i = 0; i < nums.size(); i++){
            for(int j = target; j>=0; j--){
                if(arr[j] && j + nums[i] <= target){
                    arr[j + nums[i]] = 1;
                }
            }
            if(arr[target])
                return true;
        }
        return arr[target];
    }
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for(int i = 0; i<nums.size(); i++){
            sum += nums[i];
        }
        if(sum %2 != 0)
            return false;
        return canPartition(nums, sum/2);
    }
};
