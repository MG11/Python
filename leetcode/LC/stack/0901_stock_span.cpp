#include <climits>
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class StockSpanner {
public:
    stack <int>s;
    vector <int>v;
    StockSpanner() {
    }
    
    int next(int price) {
        if(not v.size()){
            v.push_back(price);
            s.push(v.size() - 1);
            return 1;
        }
        
        while(!s.empty() && price >= v[s.top()])
            s.pop();
        int x = -1;
        if(!s.empty())x = s.top();
        v.push_back(price);
        s.push(v.size() - 1);
        return v.size() - 1 - x;
    }
};
