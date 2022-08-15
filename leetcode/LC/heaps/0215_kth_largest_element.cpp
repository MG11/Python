#include <iostream>
#include <vector>
using namespace std;
#include <queue>

/* 
take min heap, if its size becomes greater than k, pop the element, after traversing return its top.
complexity: nlog(k) where k is size of heap  n is number of elements.
*/
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater <int>> q;
        for(auto num: nums){
            q.push(num);
            if(q.size() > k){
                q.pop();
            }
        }
        return q.top();
    }
};
