#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {    
        
        if(intervals.size() < 2){
            return intervals;
        }
        sort(intervals.begin(), intervals.end(), [](vector<int> v1,vector<int> v2){
            return v1[0] < v2[0]; }); 
        
        vector<vector<int>> v;
        v.push_back(intervals[0]);
        for(int i = 1; i<intervals.size(); i++){
            if(v[v.size() -1][1] < intervals[i][0]){
                v.push_back(intervals[i]);   
            }else{
                v[v.size() -1][1] = max(v[v.size() -1][1], intervals[i][1]);
            }
        }
        return v;
    }
};
