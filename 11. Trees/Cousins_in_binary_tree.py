# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        #BFS -- TIME-O(N),space-O(N)
        if not root:
            return False
        Q = deque([root])
        while Q:
            size = len(Q)
            parent = {}
            for _ in range(size):
                node = Q.popleft()
                if node.left:
                    Q.append(node.left)
                    parent[node.left.val] = node.val
                if node.right:
                    Q.append(node.right)
                    parent[node.right.val] = node.val
                
            if x in parent and y in parent and parent[x] != parent[y]:
                return True
        return False
        
      