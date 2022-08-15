from typing import List
# O(min(n,m)) | O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if(len(nums1) > len(nums2)):
            nums1, nums2 = nums2, nums1
       
        n1 = len(nums1)
        n2 = len(nums2)
        half = (n1+n2)//2 
        lo = 0
        hi = n1 - 1
        
        while True:
            cut1 = (lo + hi)//2
            cut2 = half - cut1 - 2
            
            Aleft = nums1[cut1] if cut1 >= 0 else float('-inf')
            Aright = nums1[cut1+1] if cut1 + 1 < n1 else float('inf')
            Bleft = nums2[cut2] if cut2 >= 0 else float('-inf')
            Bright = nums2[cut2+1] if cut2 + 1 < n2 else float('inf')
            
            if Aleft > Bright:
                hi = cut1 - 1
            elif Bleft > Aright:
                lo = cut1 + 1
            else:
                if (n1 + n2)%2 == 0:
                    return (max(Aleft,Bleft) + min(Aright, Bright))/2
                else:
                    return min(Aright, Bright)
        
        