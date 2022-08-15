#include <climits>
#include <iostream>
#include <vector>
#include <stack>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int precedence(char c){
        if(c == '*' || c == '/')
            return 2;
        else
            return 1;
    }
    int evaluate(int a , int b, char c){
        switch(c){
            case '*':
                return a *b;
            case '/':
                return b/a;
            case '+':
                return a+b;
            case '-':
                return b-a;
            default:
                return 0;
                
        }
    }
    // s1 is for conversion, s2 is for evaluation
    int calculate(string s) {
        stack <char> s1;
        stack <int> s2;
        unordered_set <char> opd = {'+', '-', '*', '/'}; 
        int current_number = 0;
        for(int i = 0; i< s.length(); i++){
            if( opd.find(s[i]) != opd.end()){
                s2.push(current_number);
                current_number = 0;
                while(!s1.empty() && precedence(s1.top()) >= precedence(s[i])){
                    char c = s1.top(); s1.pop();
                    int a = s2.top(); s2.pop();
                    int b = s2.top(); s2.pop();
                    int ans = evaluate(a, b, c);
                    s2.push(ans);
                }
                s1.push(s[i]);
                
            }else{
                if(s[i] != ' ')current_number = s[i] - '0' + current_number*10 ;
            }
        }
        s2.push(current_number);
        while(!s1.empty()){
            char c = s1.top(); s1.pop();
            int a = s2.top(); s2.pop();
            int b = s2.top(); s2.pop();
            int ans = evaluate(a, b, c);
            s2.push(ans);
        }
        return s2.top();
    }
};

