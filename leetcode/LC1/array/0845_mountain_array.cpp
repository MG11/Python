#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int longestMountain(vector<int>& arr) {
        // if size is less than 3, there is no mountain
        if(arr.size() < 3){
            return 0;
        }
        int max_length = 0;
        
        int i =1;
        while(i < arr.size()){
            int left_side =0, right_side =0, sum = 0;
            int j = i;
            // traverse to the left to get left part
            while( j >= 1 && arr[j]  > arr[j-1]){
                left_side += 1;
                j--;
            }
            j = i;
            // traverse to right to get right part
            while(j < arr.size() - 1 && arr[j+1] < arr[j]){
                j++;
                right_side += 1;
            }
            i = j + 1;
            // sum is right side , left side and + 1 i.e. current peak
            sum = right_side + left_side + 1;
            if(max_length < sum && right_side && left_side){
                max_length = sum;
            }
        }
        return max_length;
        
    }
};
