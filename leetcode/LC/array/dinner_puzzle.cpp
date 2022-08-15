
// https://www.facebookrecruiting.com/portal/coding_puzzles/?c=578941846745105&puzzle=203188678289677

#include <bits/stdc++.h>
using namespace std;
// Write any include statements here

long long getMaxAdditionalDinersCount(long long N, long long K, int M, vector<long long> S) {
  // Write your code here
  long long ans = 0;
  sort(S.begin(), S.end());
  
  for(int i = S.size() -1 ; i > 0; i--){
    
    // number of ppl that can be sit b/w 2 consecutive ppl
    ans += (S[i] - S[i-1] - 1)/(K+1);
    // if last person sitting contraicts space of S[i]
    if((S[i] - S[i-1] - 1)%(K+1) != K)
      ans--;
  }
  
  // ppl sitting after last person
  ans += (N - S.back())/(K+1);
  
  // ppl sitting before first person
  ans += (S[0] -1)/(K+1);
  
  return ans;
}
