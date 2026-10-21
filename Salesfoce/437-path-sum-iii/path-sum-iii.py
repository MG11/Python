# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/path-sum-iii/editorial/

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        def pathSumHelper(node, curr_sum):
            nonlocal count
            if not node:
                return
            curr_sum += node.val
            if curr_sum == k:
                count += 1

            count += h[curr_sum - k]
            h[curr_sum] += 1
            pathSumHelper(node.left, curr_sum)
            pathSumHelper(node.right, curr_sum)

            h[curr_sum] -= 1
            return
        
        count = 0
        k = targetSum
        h = defaultdict(int)
        pathSumHelper(root, 0)
        return count


