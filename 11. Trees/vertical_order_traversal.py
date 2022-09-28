# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        #dfs
        if not root:
            return None
        column_table = defaultdict(list)
        min_column = max_column = 0
        
        def dfs(node,row,column):
            if node is not None:
                nonlocal min_column,max_column
                column_table[column].append((row,node.val))
                min_column = min(min_column,column)
                max_column = max(max_column,column)
                
                #pre-order DFS
                dfs(node.left,row +1,column-1)
                dfs(node.right,row +1,column+1)
        #DFS travel
        dfs(root,0,0)
        #extract the values from column table
        result = []
        for column in range(min_column,max_column + 1):
            result.append([val for row,val in sorted((column_table[column]))])
        return result

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        if root is None:
            return []
        column_table = defaultdict(list)
        min_column = max_column = 0
        
        def bfs(root):
            nonlocal min_column,max_column
            Q = deque([(root,0,0)])
            
            while Q:
                node,row,column = Q.popleft()
                
                if node is not None:
                    column_table[column].append((row,node.val))
                    min_column = min(min_column,column)
                    max_column = max(max_column, column)
                    
                    Q.append((node.left,row+1,column-1))
                    Q.append((node.right,row+1,column+1))
                    
        bfs(root)
        
        result = []
        for col in range(min_column,max_column+1):
            result.append([val for row,val in sorted(column_table[col])])
            
        return result
  