#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int lo = matrix[0][0];
        int s = matrix[0].size();
        int hi = matrix[s-1][s-1];
        while(lo < hi){
            int mid = lo + (hi - lo)/2;
            int count = 0;        
            // count number of elements less than mid
            
            for(int i = 0; i<=s-1;i++){
                for(int j = s-1; j>=0;j--){
                    if(matrix[i][j] <= mid){
                        count += j+1;
                        break;
                    }
                }                
            }
            if(count < k){
                lo = mid +1;
            }else{
                hi = mid;
            }
        }
        return lo;
    }
};
