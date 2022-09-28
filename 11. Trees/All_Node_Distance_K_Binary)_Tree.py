# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#TIME-O(N),SPACE--O(N)
class Solution:
    from collections import deque
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parents = {}
        self.get_parents(root,None)
        return self.bfs(target,k)
        
        #function to get the parents
    def get_parents(self,node,parent):
        if not node:
            return 
        self.parents[node] = parent
        self.get_parents(node.left,node)
        self.get_parents(node.right,node)
    
    def bfs(self,target,k):
        result = []
        visited = set()
        Q = deque([(target,0)])
        
        while Q:
            n,d = Q.popleft()
            if n not in visited:
                if d == k:
                    result.append(n.val)
                    continue
                visited.add(n)
                
                if n.left: Q.append((n.left,d+1))
                if n.right: Q.append((n.right,d+1))
                if self.parents[n]: Q.append((self.parents[n],d+1))
        return result
        
        
        

        
        
        
        