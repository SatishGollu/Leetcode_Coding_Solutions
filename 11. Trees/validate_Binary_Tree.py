# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#TIME- O(N) SPACE(N)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node,min_value,max_value):
            if not node:
                return True
            if not (node.val > min_value and node.val < max_value):
                return False
            
            return (dfs(node.left,min_value,node.val) and dfs(node.right,node.val,max_value))
        return dfs(root,float('-inf'),float('inf'))
            
#Iterative Traversal
# BFS iterative
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        Q  = deque([(root,-2**32,2**32)])
        
        while Q:
            node,low,high = Q.popleft()
            value = node.val
            if not (value > low and value < high):
                return False
            
            if node.left:
                Q.append((node.left,low,value))
            if node.right:
                Q.append((node.right,value,high))
        return True            
              
        
        