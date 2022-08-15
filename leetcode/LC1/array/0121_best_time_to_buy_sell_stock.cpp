/* traverse from left to right, keeping track of minimum element and maximum profit
*/
//O(n)/O(1)

#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minimum = INT_MAX;
        int profit = 0;
        for(int i = 0; i < prices.size(); i++){
            if((prices[i] - minimum) > profit){
                profit = prices[i] - minimum;
            }
            if(prices[i] < minimum){
                minimum = prices[i];
            }
        }
        return profit;
    }
};
