#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        
        int result = 0;
        int sum = 0;    
        while(x != 0){
            
            int q = x %10;
            x = x/10;
            
            // check if number does not fall down greater than INT_MAX / INT_MIN value
            if(sum > INT_MAX/10 || (sum == INT_MAX /10 && q > INT_MAX%10))
                return 0;
            if(sum < INT_MIN / 10 || (sum == INT_MIN/10 && q < INT_MIN % 10))
                return 0;
            
            sum = sum*10 + q;
        }
        return sum;
    }
};

