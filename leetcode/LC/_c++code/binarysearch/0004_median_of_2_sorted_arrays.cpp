#include <climits>
#include <iostream>
#include <vector>
using namespace std;


//take smaller array, mark two pointers lo and hi in that set 4 values l1, r1, l2, r2 and compare l1 > r2 or l2 > r1

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();
        
        // swap the arrays         
        if(n1 > n2){
            //smaller size will be in n1             
          return findMedianSortedArrays(nums2,nums1);
        }
        int lo = 0, hi = n1- 1, cut1 = 0, cut2 = 0;
        while(true){
            //  lo, hi are pointers on n1 (smaller array) 
            cut1 = (lo + hi) == -1 ? -1 : (lo+hi)/2;
            cut2 = (n1+n2)/2 - (cut1+2);
            
               // now find indexes of values around the cut in two arrays
               int l1 = cut1 >=0 ? nums1[cut1] : INT_MIN;
               int l2 = cut2 >= 0 ? nums2[cut2] : INT_MIN; 
               int r1 = cut1+1 >= n1 ? INT_MAX : nums1[cut1+1];
               int r2 = cut2+1 >= n2 ? INT_MAX : nums2[cut2+1];
               
                if(l1 > r2){
                    hi = cut1 - 1;
                }else if(l2 > r1){
                    lo = cut1 +1;
                }else{
                    if((n1 +n2)%2 == 0)
                        return (max(l1,l2) + min(r1,r2))/2.0;
                    else
                        return min(r1,r2);
                }
        }
        return -1;
    }
};
