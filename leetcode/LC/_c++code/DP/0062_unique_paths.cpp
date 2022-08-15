#include <vector>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector <int> dp(n+1, 0);
        dp[1] = 1;
        
        for(int i = 1; i<=m; i++){
            for(int j = 1; j <= n; j++){
                dp[j] += dp[j-1];
            }
        }
        return dp[n];
    }
};

// https://leetcode.com/problems/unique-paths-ii/

class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int row = obstacleGrid.size();
        int col = obstacleGrid[0].size();
        vector <int> dp(col+1, 0);
        dp[1] = obstacleGrid[0][0] ? 0 : 1;
        for(int i = 0; i<row; i++){
            for(int j = 1; j <= col; j++){
                if(!obstacleGrid[i][j-1])
                    dp[j] += dp[j-1];
                else
                    dp[j] = 0;
            }
        }
        return dp[col];
    }
};
