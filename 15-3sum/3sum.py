class Solution:

    def twoSum(self, i, nums, ans):
        first = nums[i]
        start = i + 1
        end = len(nums) - 1

        while start < end:
            total = first + nums[start] + nums[end]

            if total == 0:
                ans.append([first, nums[start], nums[end]])
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1
            elif total > 0:
                end -= 1
            else:
                start += 1

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        nums = sorted(nums)
        for i in range(n):
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(i, nums, ans)
        return ans
