# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
O(n) | O(logn)
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root == p or root == q:
            return root
        
        left_tree = self.lowestCommonAncestor(root.left, p, q)
        right_tree = self.lowestCommonAncestor(root.right, p,q)
        
        if left_tree and right_tree:
            return root
        
        return left_tree if left_tree else right_tree


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

"""
TC: O(N) might have to traverse all nodes
SC: O(N) BST might be skewed
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        if p.val <= root.val <= q.val:
            return root
        if p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)
