# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:

        if not root:
            return []
        queue = Deque()
        queue.append(root)

        output = []
        while len(queue):
            l = len(queue)
            ans = []
            for i in range(l):
                node = queue.popleft()
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None
                ans.append(node.val)
            output.append(ans)
        return output
