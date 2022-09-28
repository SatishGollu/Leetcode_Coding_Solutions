# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current_node = root
        
        while current_node:
            #if both values are greater than root value then go to right
            if p.val > current_node.val and q.val > current_node.val:
                current_node = current_node.right
            #if both values are less than root value then go to right
            elif p.val < current_node.val and q.val < current_node.val:
                current_node = current_node.left
            else:
                return current_node

class recursivesolution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        current_node = root
        if p.val > current_node.val and q.val > current_node.val:
                return self.lowestCommonAncestor(current_node.right,p,q)
        elif p.val < current_node.val and q.val < current_node.val:
                return self.lowestCommonAncestor(current_node.left,p,q)
        else:
            return current_node
#Recursive Time- O(logn),space-O(n)
#Iterative Time - O(logn), space-O(1)
