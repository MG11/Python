# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# preorder traversal is done here
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def serializeHelper(root, ans):
            if(root is None):
                ans.append('None')
                return
            ans.append(str(root.val))
            # print(ans)
            serializeHelper(root.left, ans)
            serializeHelper(root.right, ans)    
        ans = []

        serializeHelper(root, ans)
        result = ",".join(ans)
        print(result)
        return result  
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deserializeHelper(nodes):
            
            if not len(nodes):
                return None
            val = nodes.pop(-1)
            if val != 'null' and val != "" and val != 'None':
                root = TreeNode(val)
                root.left = deserializeHelper(nodes)
                root.right = deserializeHelper(nodes)
                return root
            else:
                return None
        nodes = data.split(',')
        nodes.reverse()
        return deserializeHelper(nodes)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
