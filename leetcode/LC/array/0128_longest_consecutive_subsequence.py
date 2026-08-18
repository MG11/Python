class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        longest = 0
        for num in nums:
            if (num - 1) in nums:
                continue
            start = num
            size = 0
            while start in nums:
                size += 1
                start += 1
            longest = max(longest, size)
        return longest


"""
This video explains how to solve the LeetCode problem **128. Longest Consecutive Sequence** efficiently.

### Core Concepts
* **Problem Definition:** Given an unsorted array of numbers, find the length of the longest sequence of consecutive integers (0:00).
* **Brute Force Approach:** Sorting the array takes $O(n \log n)$ time, which is valid but not optimal (0:34).
* **Optimal Strategy:** The goal is an $O(n)$ time complexity solution using a **Hash Set** (1:02).

### The Optimal Solution
1. **Convert to Set:** Store all numbers in a set for $O(1)$ lookups (3:44).
2. **Identify Sequence Starts:** Iterate through the numbers. A number is the start of a sequence only if `number - 1` is not in the set (2:56).
3. **Build Sequences:** Once a start is found, check for `number + 1`, `number + 2`, etc., in the set to count the sequence length (4:13).
4. **Efficiency:** Each number is visited at most twice, resulting in linear $O(n)$ time and $O(n)$ memory complexity (7:05).

### Implementation
The coding demonstration (7:23) shows how to implement this logic concisely in Python by iterating through the set and updating the `longest` count dynamically.
"""
