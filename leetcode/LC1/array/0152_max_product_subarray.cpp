#include <climits>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if(!nums.size())
            return 0;
        int max_so_far = INT_MIN;
        int min_so_far = INT_MIN;
        int result = max_so_far;
        
        for(int i = 1; i<nums.size(); i++){
            int temp = max_so_far;
            max_so_far = max(max(nums[i], nums[i]*max_so_far), nums[i]* min_so_far);
            min_so_far = min(min(nums[i], nums[i]*min_so_far), nums[i]*temp);
            if(result < max_so_far)
                result = max_so_far;
        }
        return result;
    }
};
