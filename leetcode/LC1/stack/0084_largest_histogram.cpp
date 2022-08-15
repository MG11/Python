#include <climits>
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack <int> s;
        s.push(-1);
        int maxArea = 0;
        for(int i = 0; i< heights.size(); i++){
            while(s.top() != -1 && heights[s.top()] > heights[i]){
                int height = heights[s.top()];
                s.pop();
                int currentwidth = i - s.top() - 1;
                maxArea = max(maxArea, currentwidth*height);
            }
            s.push(i);
        }
        while(s.top() != -1){
            int height = heights[s.top()];
                s.pop();
                int currentwidth = heights.size() - s.top() - 1;
                maxArea = max(maxArea, currentwidth*height);
        }
        return maxArea;
    }
};
