#include <climits>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <unordered_map>
using namespace std;

class Solution {
public:
    string alienOrder(vector<string>& words) {
        vector<int> indegree(26,-1);
        vector<vector<int>> adj(26);
        int counter = 0;
        for (auto word : words){
            for(int i = 0;i<word.length(); i++){
    
                int p = word[i] - 'a';
                // if the character is not created yet create it
                if(indegree[p] == -1){
                        indegree[p]++;
                        counter++;
                    }
            }
            }
    
    
        for(int i = 0; i< words.size() -1; i++){        
            int j = 0;
            bool inserted = false;
            while(i < words.size() -1 && words[i][j] != '\0' && words[i+1][j] != '\0'){
                int p = words[i][j] - 'a';
                int c = words[i+1][j] - 'a';    
                if(p != c){
                    indegree[c]++;
                    adj[p].push_back(c);
                    inserted = true;
                    break;
                }
                j++;
            }
            
            // for case ['abc', 'ab'] result should be ""
            if(words[i].length() > words[i+1].length() && !inserted)return "";
        }
        
            string ans;
            queue<int> q;
            // topological path, those who have 0 indegree add them in queue
            for(int i = 0; i< 26; i++){
                if(indegree[i] == 0){
                q.push(i);
            }
            }
            while(!q.empty()){
                int a = q.front();
                q.pop();
                ans += char(a + 'a');
                for(auto n : adj[a]){
                    indegree[n]--;
                    // if indegree becomes 0 push it in queue
                    if(indegree[n] == 0){
                        q.push(n);
                    }
                }
            }
            // if all characters are not coverted return "" i.e. cycle was there in words
            if(ans.length() < counter)ans = "";
            return ans;
    }
};
