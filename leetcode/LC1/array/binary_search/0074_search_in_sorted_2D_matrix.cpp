#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;


class Solution {
    // O(logmn)
    bool searchMatrix(vector<vector<int>> matrix, int target) {
        int r = matrix.size();
        int c = matrix[0].size();
        int s = 0;
        int l = r*c - 1;
        
        int mid = -1;
        // note less than or equal to
        while(s <= l){
            mid =  (l -s)/2 + s;
            // mid / c will give number of rows passed and mid %c will give number of columns passed
            if(matrix[mid/c][mid%c] == target){
                return true;
            }else if(matrix[mid/c][mid%c] > target){
                l = mid  - 1;
            }else{
                s = mid + 1;
            }  
        }
        return false;
    }
};
