#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int maxlen = 0, start = 0;
    void expandAroundCentres(string s, int l, int r){
        while(l >=0 && r <s.length() && s[l] == s[r]){
            l--;
            r++;
        }
        l++;
        r--;
        if(maxlen < r - l +1){
            maxlen = r - l +1;
            start = l;
        }
    }
    
    string longestPalindrome(string s) {
        for(int i = 0; i< s.length(); i++){
            expandAroundCentres(s, i, i);
            expandAroundCentres(s, i , i+1);
        }
        return s.substr(start,maxlen);
    }
};
