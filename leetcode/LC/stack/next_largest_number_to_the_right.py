https://bytebytego.com/exercises/coding-patterns/stacks/next-largest-number-to-the-right


from typing import List

def next_largest_number_to_the_right(nums: List[int]) -> List[int]:
    # Write your code here
    res = [-1]*len(nums)
    stack = []

    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(nums[i])
    return res
