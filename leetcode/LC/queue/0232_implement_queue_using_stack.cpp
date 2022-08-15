/* 
push is always on stack 1, pop always from stack 2, when stack 2 is empty, pop elements from S1 and push them in stack 2.
*/


#include <stack>
using namespace std;

class MyQueue {
public:
    stack <int> s1, s2;
    MyQueue() {}
    
    void push(int x) {
        s1.push(x);
    }
    
    int pop() {
        move();
        int x = s2.top();
        s2.pop();
        return x;
    }
    
    int peek() {
        move();
        return s2.top();
    }
    
    bool empty() {
        return s1.empty() && s2.empty();
    }
    
    void move(){
        if(s2.empty()){
            while(!s1.empty()){
                int x = s1.top();
                s1.pop();
                s2.push(x);
            }
        }
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */