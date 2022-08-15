# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodeHelper(self, root, maxallowed, res):
        if not root:
            return
        if root.val >= maxallowed:
            res[0] += 1
            maxallowed = root.val
        self.goodNodeHelper(root.left, maxallowed, res)
        self.goodNodeHelper(root.right, maxallowed, res)
        
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = [0]
        self.goodNodeHelper(root, float('-inf'), res)
        return res[0]
