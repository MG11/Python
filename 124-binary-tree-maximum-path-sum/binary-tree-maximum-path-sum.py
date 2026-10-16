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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution1:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = float('-inf')

        def maxPathSumHelper(root):
            nonlocal maxVal
            if not root:
                return 0
            val = root.val
            leftval = max(maxPathSumHelper(root.left), 0)
            rightval = max(maxPathSumHelper(root.right), 0)
            maxVal = max(maxVal, val + leftval + rightval)
            return max(leftval, rightval) + val
        
        val = maxPathSumHelper(root)
        return max(maxVal, val)
