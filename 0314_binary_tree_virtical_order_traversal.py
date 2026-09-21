# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        queue = deque([(root, 0)])
        cols = defaultdict(list)

        min_col, max_col = 0, 0

        while queue:
            node, col = queue.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            cols[col].append(node.val)
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))
        output = []
        for i in range(min_col, max_col + 1):
            output.append(cols[i])
        return output
