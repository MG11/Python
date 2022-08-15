# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        while(len(q)):
            result = []
            size = len(q)
            for i in range(size):
                node = q.popleft()
                result.append(node.val)
                if node.left:
                    q.append(node.left) 
                if node.right:
                    q.append(node.right)
            ans.append(result)
        return ans
    