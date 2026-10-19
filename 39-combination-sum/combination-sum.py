class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        candidates.sort()

        def helper(start, target, data):
            nonlocal ans
            if target == 0:
                ans.append(data[:])
                return
            if target < 0:
                return
            
            if start < len(candidates):
                data.append(candidates[start])
                helper(start, target - candidates[start], data)
                data.pop()
                helper(start + 1, target, data)

        
        helper(0, target, [])
        return ans

        