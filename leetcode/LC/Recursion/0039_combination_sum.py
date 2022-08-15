from typing import List

# https://leetcode.com/problems/combination-sum/solution/ for time complexity

class Solution:
    def __init__(self):
        self.ans = []
    
    def cdH(self, candidates, index, target, output):
        if(target < 0):
            return
        if(target == 0):
            self.ans.append(output.copy())
            return
        
        for i in range(index, len(candidates)):
            # self.cdH(candidates, target, output)
            if(target - candidates[i] >= 0):
                output.append(candidates[i])
                self.cdH(candidates, i, target - candidates[i], output)
                output.pop()
        
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.cdH(candidates, 0, target, [])
        return self.ans
