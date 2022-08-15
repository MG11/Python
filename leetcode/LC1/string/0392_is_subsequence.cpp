#include <string>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int ss = 0;
        int st = 0;
        
        // ss is pointer on s, st is pointer on t
        while(ss < s.size() && st < t.size()){
            if(s[ss] == t[st]){
                ss++;
                st++;
            }else{
                st++;
            }
        }
        return (ss == s.size());
        
        
    }
};
