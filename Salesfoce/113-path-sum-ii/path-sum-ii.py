# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        data = []
        ans = []
        if not root:
            return []

        def pathSumHelper(root, target):
            nonlocal ans
            nonlocal data

            if not root:
                return

            if target == root.val and not root.left and not root.right:
                data.append(root.val)
                ans.append(data[:])
                data.pop()
                return
            
            data.append(root.val)
            pathSumHelper(root.left, target - root.val)
            pathSumHelper(root.right, target - root.val)
            data.pop()

        pathSumHelper(root, targetSum)
        return ans
        