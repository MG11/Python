/*
if current value is equal to previous, then counter++
else counter will reset to 1 and insert char and counter.
*/
#include<iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
    
private:
    vector<char> charTemp;
    void changeString(char chars, int initial){
        charTemp.push_back(chars);
        if (initial > 1){
        string str = to_string(initial);
        
        int i = 0;
        while(str[i] != '\0'){
            charTemp.push_back(str[i]);
            i++;
        }
        }
    } 
    
public:
    int compress(vector<char>& chars) {
        if(chars.size() <= 1){
            return chars.size();
        }
        int initial = 1;
        int i = 1;
        for(i = 1; i< chars.size(); i++){
            if(chars[i] == chars[i-1]){
                initial++;
            }else{
                changeString(chars[i-1], initial);
                initial = 1;
            }
        }
        changeString(chars[i-1], initial);
        for(int i = 0; i< charTemp.size(); i++){
            chars[i] = charTemp[i];
        }
        return charTemp.size();
    }
};
