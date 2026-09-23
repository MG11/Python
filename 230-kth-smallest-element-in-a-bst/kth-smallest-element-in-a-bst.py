# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        def kthsmallestHelper(root):
            nonlocal k
            if not root:
                return None
            val = kthsmallestHelper(root.left)
            if val is not None:
                return val
            print(root.val, k)
            if (k == 1):
                return root.val
            k -= 1
            val = kthsmallestHelper(root.right)
            if val is not None:
                return val
        return kthsmallestHelper(root)
