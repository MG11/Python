class Solution:
    def jump(self, nums: List[int]) -> int:
        i, j = 0, 0
        n = len(nums)
        jump = 0
        while (i < n - 1):
            if nums[i] == 0:
                return -1
            maxj = 0
            maxi = i
            for j in range(i + 1, nums[i] + i + 1):
                if (j == n - 1):
                    maxi = j
                    break
                if (nums[j] + j >= maxj):
                    maxj = nums[j] + j
                    maxi = j
            i = maxi

            jump += 1

        return jump