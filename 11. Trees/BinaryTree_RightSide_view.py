#1 BFS solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #TIME- O(N), Space - O(D) tree diameter
    from collections import deque
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        q = deque([root])
        
        while q:
            rightside = None
            qlen = len(q)
            
            for each in range(qlen):
                node = q.popleft()
                if node:
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                result.append(rightside.val)
        return result

#2 a liitle easier code
class Solution:
    #TIME- O(N), Space - O(D) tree diameter
    from collections import deque
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        q = deque([root])
        
        while q:
            lenq = len(q)
            
            for i in range(lenq):
                node = q.popleft()
                if i == lenq-1:
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result
# DFS version

          