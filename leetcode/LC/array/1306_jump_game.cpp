#include <unordered_set>
#include <vector>
using namespace std;

//https://www.youtube.com/watch?v=dJ7sWiOoK7g
// jump game 2
// take left and right pointers, these are the ranges i can land from previous point.
// now, from these range find farthest point in can reach that will be my right and left will be right +1

class Solution1 {
public:
    int jump(vector<int>& nums) {
        int left = 0, right = 0, res = 0;
        
        while (right < nums.size() -1){
            int farthest = 0;
            for(int i = left; i<= right; i++){
                farthest = max(farthest, nums[i] +i);
            }
            left = right + 1;
            right = farthest;
            res++;
        }
        return res;
    }
};


// jump game 1
bool canJump(vector<int> &nums){
        int left = 0, right = 0, farthest = 0;
        int l = nums.size();
        while(left <= right){ // in case of it can never reach, right will become more
            if(right >= l-1)return true; // if right is more than length of nums it can reach
            for(int i = left; i <= right; i++){
                 farthest = max(farthest, nums[i] + i);
             }
            left = right + 1;
            right = farthest;
        }
        return false;
    }


// jump game 3

class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
      if(start < 0 || start >= arr.size() || arr[start] < 0)
          return false;
      if(arr[start] == 0)return true;
      // changed the array so that we not start checking this again     
      arr[start] = (-1)*arr[start];
    // check for arr[start] steps forward and backward
     return canReach(arr, start + arr[start]) || canReach(arr, start - arr[start]);           
    }
};
