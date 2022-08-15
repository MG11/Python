#include <climits>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int size = nums.size();
        int sum = size*(size + 1)/2;
        for(int i = 0; i < nums.size(); i++){
            sum -=nums[i];
        }
        return sum;
    }
};
