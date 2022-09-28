# My way using queue and map of map
#TIME-O(N), Space O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        #BFS
        level_map = defaultdict(list)
        Q = deque([(root,0)])
        
        while Q:
            node,level = Q.popleft()
            
            level_map[level].append(node.val)
            
            if node.left:
                Q.append((node.left, level + 1))
            if node.right:
                Q.append((node.right, level + 1))
        
        result = []
        for levels,vals in level_map.items():
            result.append(vals)
        return result

# Better run time
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        #BFS
        levels = []
        Q = deque([(root,0)])
        
        while Q:
            node,level = Q.popleft()
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            
            if node.left:
                Q.append((node.left, level + 1))
            if node.right:
                Q.append((node.right, level + 1))
        
        return levels

