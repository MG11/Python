#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
    private: 
    vector<vector<int>> ans;
    
    void my_subset(vector<int>& nums, int index, vector<int>& output){
        if(nums.size() == index){
            ans.push_back(output);
            return;
        }
        my_subset(nums, index+1, output);
        output.push_back(nums[index]);
        my_subset(nums, index+1, output);
        output.pop_back();
        return;
        }
    
    public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> output = {};
        my_subset(nums, 0, output);
        return ans;
    }
};

// optimized 

class Solution2 {
    private: 
    vector<vector<int>> ans;
    
    void my_subset(vector<int>& nums, int index, vector<int>& output){
        ans.push_back(output);
        for(int i = index; i< nums.size(); i++){
            output.push_back(nums[i]);
            my_subset(nums, i+1, output);
            output.pop_back();
        }
        }
    
    public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> output = {};
        my_subset(nums, 0, output);
        return ans;
    }
};

