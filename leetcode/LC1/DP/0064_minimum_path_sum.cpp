#include <vector>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int col = grid[0].size();
        int row = grid.size();
        
        vector<int> dp (col, 0);
        dp[0] = grid[0][0];
        for(int i = 1; i < col; i++)
            dp[i] = grid[0][i] + dp[i-1];
        
        for(int i = 1; i< row; i++){
            for(int j = 0; j< col; j++){
                if(j == 0)
                    dp[j] += grid[i][j];
                else
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j];
            }
        }
        return dp[col-1];
    }
};
