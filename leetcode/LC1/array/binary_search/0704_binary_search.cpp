#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;


class Solution {
    int search(vector <int> nums, int target) {
        int low = 0;
        int high = nums.size() -1;
        
        while(low <= high){
            int mid = (low + high) / 2;
            
            if (nums[mid] == target){
                return mid;
            }else if(nums[mid] > target){
                high = mid -1;
            }else{
                low = mid +1;
            }
            
        }
        return -1;
    }
};

// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

bool isBadVersion(int mid){
    return true;
};

class Solution2 {
public:
    int firstBadVersion(int n) {
        int left = 1;
        int right = n;
        int ans = n;
        
        while(left <= right){
            int mid = left + (right - left)/2;
            
            if(isBadVersion(mid)){
                ans = mid;
                right = mid -1;
            }else{
                left = mid + 1;
            }
        }
        return ans;
        
    }
};
