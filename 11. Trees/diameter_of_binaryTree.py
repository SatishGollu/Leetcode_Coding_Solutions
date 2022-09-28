#printing diameter and nodes too.

def __init__(self):
    self.diameter = 0
    self.diameterPath = []      

def diameterOfBinaryTree(self, root) -> int:    
    def dfs(node):
        if(not node):
            return 0,[]
        
        curPath = []
        left,leftPath = dfs(node.left)
        right, rightPath = dfs(node.right)
        
        if((left+right) > self.diameter):
            self.diameter = left+right
            self.diameterPath = leftPath + [node.val] + rightPath[::-1]
        
        if(left>right):
            leftPath.append(node.val)
            curPath = leftPath
        else:
            rightPath.append(node.val)
            curPath = rightPath
            
        return (1+max(left,right)),curPath
    
    dfs(root)
    print(self.diameterPath)
    return self.diameter


# just the diameter
def diameterOfBinaryTree(self, root):
    diameter = 0
    #DFS, 
    def dfs(node):
        nonlocal diameter
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        
        if (left+right) > diameter:
            diameter = (left+right)
        return max(left,right) + 1
    dfs(root)
    return diameter