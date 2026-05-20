# time complexity: n*2^n : n to copy elements in result, 2^n are the total number of subsets formed,
# space complexity: n, which is height of resursion tree.

class Solution:
    output = []
    def subsethelper(self, nums, i, data):
        if i == len(nums):
            self.output.append(data[:])
            return
        data.append(nums[i])
        self.subsethelper(nums, i + 1, data)
        data.pop()
        self.subsethelper(nums, i + 1, data)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        self.subsethelper(nums, 0, [])
        return self.output
