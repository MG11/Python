# https://www.youtube.com/watch?v=Osz-Vwer6rw

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSumHelper(self, root, res):
        if not root:
            return 0
        l = self.maxPathSumHelper(root.left, res)
        r = self.maxPathSumHelper(root.right, res)

        temp = max(l + root.val, r + root.val, root.val)
        ans = max(temp, l + r + root.val)
        res[0] = max(ans, res[0])
        return temp

    def maxPathSum(self, root: TreeNode | None) -> int:
        res = [float('-inf')]
        self.maxPathSumHelper(root, res)
        return res[0]
