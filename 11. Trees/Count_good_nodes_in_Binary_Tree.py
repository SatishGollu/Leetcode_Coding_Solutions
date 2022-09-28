# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.max_val = root.val
        def dfs(root,max_val):
            if not root:
                return 0
            if root.val >= max_val:
                self.count += 1
                max_val = root.val
            dfs(root.left,max_val)
            dfs(root.right,max_val)
        max_va = root.val
        dfs(root,max_va)
        return self.count
            
# BFS

class Solution:
    from collections import deque
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        #bfs
        result = 0
        Q = deque([(root,root.val)])
        
        while Q:
            node,max_so_far = Q.popleft()
            if node.val >= max_so_far:
                result += 1
                max_so_far = node.val
            
            if node.left:
                Q.append((node.left,max_so_far))
            if node.right:
                Q.append((node.right,max_so_far))
        return result
                
                      
                
            
                
        