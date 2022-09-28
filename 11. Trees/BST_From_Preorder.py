# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        index = 0
        #recursive approach TIME--O(N),space _O(N)
        def recurs(lower,higher):
            nonlocal index
            if index == n:
                return None
            value = preorder[index]
            if value < lower or value > higher:
                return None
            index += 1
            root = TreeNode(value)
            root.left = recurs(lower,value)
            root.right = recurs(value,higher)
            return root
        #length 
        n = len(preorder)
        return recurs(float('-inf'),float('inf'))
            
        