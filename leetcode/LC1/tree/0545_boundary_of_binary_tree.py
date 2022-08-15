from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leftboundary(self, root, ans):
        # if it root is None or it is leaf node
        if(root is None or not (root.left or root.right)):
            return
        ans.append(root.val)
        if(root.left):
            self.leftboundary(root.left, ans)
        else:
            self.leftboundary(root.right, ans)
    
    
    def rightboundary(self, root, ans):
        if(root is None or not (root.left or root.right)):
            return
        if(root.right):
            self.rightboundary(root.right, ans)
        else:
            self.rightboundary(root.left, ans)
        # in rigt boundary append at last
        ans.append(root.val)
        
    def leaves(self, root,ans):
        if(root is None):
            return
        if(not (root.left or root.right)):
            ans.append(root.val)
        self.leaves(root.left, ans)
        self.leaves(root.right, ans)
        
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if(root is None):
            return None
        ans.append(root.val)
        self.leftboundary(root.left, ans)
        if(root.left or root.right):
            self.leaves(root, ans)
        self.rightboundary(root.right, ans)
        return ans
        