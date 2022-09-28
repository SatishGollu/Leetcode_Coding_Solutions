# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TIME_ O(N), space - O(N)
class Solution:
    from collections import defaultdict,deque
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        mapping = defaultdict(list)
        Q = deque([(root,0)])
        result = []
        while Q:
            node,diameter = Q.popleft()
            if node:
                mapping[diameter].append(node.val)
                if node.left:
                    Q.append((node.left,diameter + 1))
                if node.right:
                    Q.append((node.right,diameter + 1))
            # taking elements 
        for index,values in mapping.items():
            if index % 2 == 0:
                result.append(values)
            else:
                result.append(values[::-1])
        return result
        