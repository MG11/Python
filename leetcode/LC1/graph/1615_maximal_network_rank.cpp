#include <climits>
#include <iostream>
using namespace std;
#include <vector>

// take 1 1D vector to store road count, and one 2D vector to store connections
class Solution {
public:
    int maximalNetworkRank(int n, vector<vector<int>>& roads) {
        int max_rank = 0;
        vector<int> v(n,0);
        vector<vector<int>> connect(n, vector<int>(n,0));
        
        for(int i = 0; i< roads.size(); i++){
        
            v[roads[i][0]]++;
            v[roads[i][1]]++;
            connect[roads[i][0]][roads[i][1]] = 1;
            connect[roads[i][1]][roads[i][0]] = 1;
        }
        
        for(int i = 0; i<n ;i++){
            for(int j = i+1; j < n; j++){
                max_rank = max(max_rank, v[i] + v[j] - connect[i][j]);
            }
        }
        return max_rank;
    }
};
