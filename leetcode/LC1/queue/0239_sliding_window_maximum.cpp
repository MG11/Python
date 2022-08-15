#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#include <unordered_map>
#include <queue>

// https://leetcode.com/problems/sliding-window-maximum/discuss/65885/This-is-a-typical-monotonic-queue-problem/202024
/*
monoqueue will work as follows :
1) 5 2 3 1 5 
5 
5 2 
5 3 
5 3 1 
5 5 
front will give maximum
 */

/*
 TC: O(n) where push is aromatised
 SC: O(K)
*/

class monoqueue{
    deque <int> q;
    public:
    void push(int data){
        while(!q.empty() && q.back() < data){
            q.pop_back();
        }
        q.push_back(data);
    }
    
     void pop(int n){
         if(q.front() == n)
             q.pop_front();
     }
    
    int front(){
        return q.front();
    }
};

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        monoqueue mq;
        vector <int> ans;
        for(int i = 0; i< nums.size(); i++){
            if(i < k-1){
                mq.push(nums[i]);
            }else{
                mq.push(nums[i]);
                ans.push_back(mq.front());
                // if the front element is the element to be removed then remove that.
                mq.pop(nums[i+1-k]);
            }
        }
        return ans;
    }
};
