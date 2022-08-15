/*
traverse 1 array, put its value and count in set.
traverse 2nd array, check if it is in set and decrease set value
https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82243/Solution-to-3rd-follow-up-question
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
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        
        unordered_map <int, int> s;
        
        for(int i = 0 ; i <nums1.size(); i++){
            if(s.count(nums1[i]) != 0)
                s[nums1[i]]++;
            else{
                s[nums1[i]] = 1;
            }
        }
        
        vector<int> ans;
        
        for(int i = 0; i< nums2.size(); i++){
            if(s.count(nums2[i]) != 0 && s[nums2[i]] != 0){
                s[nums2[i]]--;
                ans.push_back(nums2[i]);
            }
        }
        return ans;
    }
};
