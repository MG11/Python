#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <unordered_map>
using namespace std;

//dijkastra algorithm, also check heap approach https://leetcode.com/problems/network-delay-time/solution/

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // create adjacency list with initial node as graph index and values as vector of pairs with values target node and weight.
        vector<vector<pair<int, int>>>graph(n+1); // {targetnode, wt}
        for(auto time: times){
            graph[time[0]].push_back({time[1], time[2]});
        }
        
        // set distance of all node from target nodes to infinity
        vector<int> distance(n+1, INT_MAX);
        // take ordered set to get node with minimum weight till now.
        set <pair<int,int>> s; // {wt, target node}
        s.insert({0, k});
        distance[k] = 0;
        distance[0] = 0;
        while(!s.empty()){
            auto x = *(s.begin());
            s.erase(x);
            for(auto time: graph[x.second]){
                //cout<< time.first <<" "<<time.second<<endl;
                if(distance[time.first] > x.first + time.second){
                    distance[time.first] = x.first + time.second;
                    s.insert({distance[time.first], time.first});
                }
            }
        }
        int ans = *max_element(distance.begin(), distance.end());
        if (ans == INT_MAX)ans = -1;
        return ans;
    }
};
