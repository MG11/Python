# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def parentMap(self, root, start):
        pmap = {}
        inode = None

        def dfs(root):
            nonlocal inode
            if root is None:
                return
            if root.val == start:
                inode = root
            if root.left:
                pmap[root.left] = root
                dfs(root.left)
            if root.right:
                pmap[root.right] = root
                dfs(root.right)
        dfs(root)
        return inode, pmap

    def bfs(self, root, inode, pmap):
        q = deque()
        q.append(inode)
        maxi = 0
        visited = {}
        if inode:
            visited[inode.val] = 1
        while len(q):
            l = len(q)
            for i in range(l):
                n = q.popleft()
                if n.left is not None and n.left.val not in visited:
                    q.append(n.left)
                    visited[n.left.val] = 1
                if n.right is not None and n.right.val not in visited:
                    q.append(n.right)
                    visited[n.right.val] = 1
                parent = pmap.get(n)
            
                if parent and parent.val not in visited:
                    q.append(parent)
                    visited[parent.val] = 1
            maxi += 1
        return maxi
            
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
         # first create a hash map, storing part
         # find node of start
         # do bfs to burn and find time

         inode, pmap = self.parentMap(root, start)
         time = self.bfs(root, inode, pmap)
         return time - 1
