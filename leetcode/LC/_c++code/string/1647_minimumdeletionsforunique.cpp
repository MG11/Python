/* 
O(n) | O(1)
LC: 1647
*/
#include<iostream>
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int minDeletions(string s) {
        int arr[26] = {0};
        
        for(int i = 0; i<s.length(); i++){
            arr[int(s[i]) - 97]++;
        }
        
        int ans = 0;
        
        unordered_set<int> visited;
        
        for(int i = 0; i < 26; i++){
            
            while(visited.find(arr[i]) != visited.end()){
                ans++;
                arr[i]--;
            }
            if(arr[i] > 0)visited.insert(arr[i]);
        }
        return ans;
    }
};
