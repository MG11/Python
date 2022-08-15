#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <unordered_map>
using namespace std;


class Solution {
public:
 
    int maxRow;
    int maxCol;
    void dfs(int r, int c,  vector<vector<bool>>& v, int& height, vector<vector<int>>& heights){
        if(r < 0 or r > maxRow or c < 0 or c > maxCol or heights[r][c] < height or v[r][c])
           return;
        v[r][c] = true;
        vector<vector<int>> directions = {{r+1, c}, {r-1, c}, {r, c+1}, {r, c-1}};
           for(auto dir: directions){
               dfs(dir[0], dir[1], v, heights[r][c], heights);
           }
    }
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        
        int r = heights.size();
        int c = heights[0].size();
        maxRow = r-1;
        maxCol = c-1;
        vector<vector<bool>> p(r, vector<bool>(c, false));
        vector<vector<bool>> a(r, vector<bool>(c, false));
        for(int i = 0; i< heights[0].size(); i++){
            dfs(0, i, p, heights[0][i], heights);
            dfs(r-1, i, a, heights[r-1][i], heights);
        }
        for(int i = 0; i< heights.size(); i++){
            dfs(i, 0, p, heights[i][0], heights);
            dfs(i, c-1, a, heights[i][c-1], heights);
        }
        vector<vector<int>>ans;
        for(int i = 0; i< r; i++){
            for(int j = 0; j< c; j++){
                if(p[i][j] && a[i][j])
                    ans.push_back({i,j});
            }
        }
        return ans;        
    }
};
