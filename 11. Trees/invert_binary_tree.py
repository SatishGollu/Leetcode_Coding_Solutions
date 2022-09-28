#Time-O(N),Space-O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        #post order recursive
        if not root:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        invert = root.left
        root.left = root.right
        root.right = invert
        return root

#   ITERATIVE
class Solution:
    def invertTree(self, root):
        #iterative
        if not root:
            return None
        Q = collections.deque([root])
        while Q:
            node = Q.popleft()
            node.left,node.right = node.right,node.left
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
        return root
        
        