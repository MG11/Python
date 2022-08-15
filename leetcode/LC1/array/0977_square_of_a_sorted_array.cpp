#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

// ex: [-150, -120, -90, 0, 10, 100] use two pointers to left most and right most and find maximum absolute
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int i = 0;
        int j = nums.size() - 1;
        vector<int> v;
        while(i <= j){
            if(abs(nums[i]) > abs(nums[j])){
                v.push_back(nums[i]*nums[i]);
                i++;
            }else{
                v.push_back(nums[j]*nums[j]);
                j--;
            }
        }
        reverse(v.begin(), v.end());
        return v;
    }
    
};
