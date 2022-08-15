#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

// TC: O(n), O(n)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> indics;
        
        unordered_map<int, int> compliment;
        
        for(int i = 0; i<nums.size(); i++){
            if(compliment.count(target - nums[i]) != 0){
                return {i, compliment[target - nums[i]]};
            }else{
                compliment[nums[i]] = i;
            }
        }
        return indics;
    }
};

// class Solution:
//     def twoSum(self, nums: List[int], target: int) -> List[int]:
//         my_dict = dict()
//         for i in range(len(nums)):
//             if (target - nums[i]) in my_dict:
//                 return [i, my_dict[target - nums[i]]]
//             my_dict[nums[i]] = i
                