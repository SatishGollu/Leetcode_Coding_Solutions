# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    # DFS method- TIme--O(N), Space -O(N)
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        def dfs(node):
            if not node:
                result.append("N")
                return 
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0
        
        def dfs():
            #base
            if vals[self.i] == "N":
                self.i += 1
                return
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))



# BFS METHOD
class codec:
    # O(N) time and O(N) space
    def serialize(self,root):
        if not root:
            return ''
        q = deque([root])
        vals = []
        while q:
            node = q.popleft()
            if node is None:
                vals.append("N")
                continue
            vals.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return ",".join(vals)
    
    def deserialize(self,data):
        if not data:
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q and i < len(vals):
            node = q.popleft()
            if val[i] != None:
                left = TreeNode(int(vals[i]))
                node.left = left
                q.append(left)
            i += 1
            if val[i] != None:
                right = TreeNode(int(vals[i]))
                node.right = right
                q.append(right)
            i += 1
        return root
        