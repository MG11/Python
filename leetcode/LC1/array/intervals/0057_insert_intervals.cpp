#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#include <unordered_map>
#include <queue>


class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> ans;
        int i = 0;
        // insert those meetings which started early
        for(i = 0; i<intervals.size(); i++){
            if(intervals[i][0] <= newInterval[0]){
                ans.push_back(intervals[i]);
            }
            else break;
        }
        cout<<ans.size();
        // now, add interval..
        if(ans.size() && ans.back()[1] >= newInterval[0]){
                ans[ans.size() - 1][1] = max(newInterval[1], ans.back()[1]);
            }else{
                ans.push_back(newInterval);
        }
        
        // insert rest of the intervals..
        for(int j = i; j<intervals.size(); j++){
            if(ans.back()[1] >= intervals[j][0]){
                ans[ans.size() - 1][1] = max(intervals[j][1], ans.back()[1]);
            }else{
                ans.push_back(intervals[j]);
            }
        }
        return ans;
    }
};
