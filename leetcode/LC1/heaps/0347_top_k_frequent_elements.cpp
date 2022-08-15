#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#include <unordered_map>
#include <queue>

/* 
store elements in unordered map with their frequency, 
after that store top k elements in queue with their frequency and value
create array with values
*/

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map <int, int> m;
        for(auto num: nums){
            if(m.find(num) != m.end()){
                m[num] += 1;
            }else{
                m[num] = 1;
            }
        }
        priority_queue <pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
        for(auto freq: m){
            q.push({freq.second, freq.first});
            if(q.size() > k){
                q.pop();
            }
        }
        vector <int> ans;
        while(q.size()){
            auto s = q.top();
            ans.push_back(s.second);
            q.pop();
        }
        return ans;
    }
};
