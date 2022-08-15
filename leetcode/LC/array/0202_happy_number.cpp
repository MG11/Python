// use fast and slow pointer to detect cycle

class Solution {
public:
    int getnext(int n){
        int sum = 0;
        while(n){
            int x = n%10;
            n = n/10;
            sum += x*x;
        }
        return sum;
    }
    bool isHappy(int n) {
        int slow = n;
        int fast = getnext(n);
        while(slow != 1 && fast != slow){
            slow = getnext(slow);
            fast = getnext(getnext(fast));
        }
        return fast == 1;
    }
};