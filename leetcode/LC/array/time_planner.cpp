/* Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return null.

Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. The input variable dur is a positive integer that represents the duration of a meeting in seconds. The output is also a pair represented by an epoch array of size two.

In your implementation assume that the time slots in a person’s availability are disjointed, i.e, time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.

Implement an efficient solution and analyze its time and space complexities. */

// https://www.pramp.com/challenge/3QnxW6xoPLTNl5jX5Lg1

#include <iostream>
#include <vector>

using namespace std;

vector<int> meetingPlanner( const vector<vector<int>>& slotsA, const vector<vector<int>>& slotsB, int dur) 
{
  // your code goes here
    int i = 0, j = 0;
    for(i = 0, j = 0; i <slotsA.size(), j < slotsB.size(); ){
      int first = max(slotsA[i][0], slotsB[j][0]);
      int second = min(slotsB[i][1], slotsB[j][1]);
      if(second - first >= dur){
        return {first, first+dur};
      }
      if(slotsB[j][1] < slotsA[i][1]) j++;
      else i++;
    }
    return {};
}

int main() {
  vector<vector<int>> slota = {{10,50}, {60,120}, {140, 210}};
  vector<vector<int>> slotb = {{0,15}, {60, 70}};
  vector<int> ans = meetingPlanner(slota, slotb, 12);
  if(ans.size())cout<<ans[0] << " "<<ans[1]<<endl;
  else cout<<"no slot found";
  return 0;
}

// https://www.linkedin.com/in/aayushi-khandelwal-451a99a2/
