/*

1) traverse from left to right to get minimum to the left of a bar.
2) traverse from right to left to get minimum to the right of a bar.

3) for each bar find water stored like —> Min(L[i], R[i]) - Bar[i])
*/
#include <unordered_set>
#include <vector>
using namespace std;

// O(n) | O(n)
class Solution1 {
public:
    int trap(vector<int>& height) {
        vector<int> left(height.size(), 0);
        vector<int> right(height.size(), 0);
        
        int maxi = height[0];
        for(int i = 0; i<height.size(); i++){
            if(height[i] > maxi){
                left[i] = height[i];
                maxi = height[i];
            }else{
                left[i] = maxi;
            }
        }
        maxi = height.back();
        for(int i = height.size() - 1; i>=0; i--){
            if(height[i] > maxi){
                right[i] = height[i];
                maxi = height[i];
            }else{
                right[i] = maxi;
            }
        }
        int count = 0;
        for(int i = 0; i< height.size(); i++){
            int water = min(left[i], right[i]) - height[i];
            int currentWater = water > 0 ? water : 0;
            count += currentWater;
        }
        return count;
    }
};


// two pointers approach, O(n) | O(1)
class Solution {
public:
    int trap(vector<int>& height) {
        int count = 0;
        int left = 0, right = height.size() - 1;
        int lmax = height[0], rmax = height[right];
        while(left <= right){
            if(lmax <= rmax){
                count += max(lmax - height[left], 0);
                lmax = lmax > height[left]  ? lmax: height[left];
                left++;   
            }
            else{
                count += max(rmax - height[right], 0);
                rmax = rmax > height[right]  ? rmax : height[right];
                right--;
                 
            }
        }
        return count;
    }
};
