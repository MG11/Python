#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#include <queue>

class Interval{
    public:
    int start;
    int end;
};

class Solution {
public:
    /**
     * @param intervals: an array of meeting time intervals
     * @return: the minimum number of conference rooms required
     */
    int minMeetingRooms(vector<Interval> &intervals) {
        // Write your code here
        if(!intervals.size())
            return 0;
        sort(intervals.begin(), intervals.end(), [](auto a, auto b){return a.start < b.start;});
        int ans = 1;
        priority_queue <int, vector<int>, greater<int> > pq;
        pq.push(intervals[0].end);

        for(int i = 1; i<intervals.size(); i++){
            cout<<pq.top()<<endl;
            if(pq.top() > intervals[i].start){
                // need more rooms
                pq.push(intervals[i].end);
                ans++;
            }else{
                pq.pop();
                pq.push(intervals[i].end);
            }
        }
        return ans;
    }
};
