#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max_length = 0;
        int current_sum = 0;
        
        // to get position of a char in string
        unordered_map <char, int> m;
        // window start index
        int i = 0;
        // window end index
        int j = 0;

        for(int j = 0; j<s.length(); j++){
            // if i found same character in string, after window start index then make window start after the current char index
            if(m.count(s[j]) != 0 && m[s[j]] >=i){
                i = m[s[j]] +1;
                current_sum = j - i +1;  
            }else{
                current_sum += 1;
            }
        m[s[j]] = j; 
        max_length = max(max_length, current_sum);
        }
        return max_length;
    }
};
