from typing import List

# https://leetcode.com/problems/combination-sum/solution/ for time complexity

class Solution:
    def __init__(self):
        self.output = []

    def combinationSumHelper(self, candidates, i, target, data):
        if target < 0:
            return
        if target == 0:
            self.output.append(data[:])
            return
        if i < len(candidates):
            data.append(candidates[i])
            self.combinationSumHelper(candidates, i, target - candidates[i], data)
            data.pop()
            self.combinationSumHelper(candidates, i + 1, target, data)


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output = []
        self.combinationSumHelper(sorted(candidates), 0, target, [])
        return self.output

