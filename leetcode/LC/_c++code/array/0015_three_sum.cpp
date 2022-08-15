#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    
    void twosum(vector<int>& nums, int i, vector<vector<int>> &triplets){
        int start = i +1;
            int end = nums.size() - 1;
            while(start < end){
                
                if(nums[i] + nums[start] + nums[end] == 0){
                    triplets.push_back({nums[i], nums[start], nums[end]});
                    start++;
                    end--;
                    while(start < end && nums[start] == nums[start - 1])
                        start++;
                    while(start < end && nums[end] == nums[end+1])
                        end--;
                }else if(nums[i] + nums[start] + nums[end] > 0){
                    end--;
                }else{
                    start++;
                }
            }   
    }
    
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        sort(nums.begin(), nums.end());
        vector<vector<int>> triplets;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] > 0){
                break;
            }
            if(i != 0 && nums[i] == nums[i-1]){
                continue;
            }
            twosum(nums, i, triplets);
        }
        return triplets;
    }
};
