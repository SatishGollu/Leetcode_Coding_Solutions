#BFS
#TIME - O(E+V)

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import defaultdict,deque
class BFS_Solution:
    def cloneGraph(self, node):
        #BFS
        if not node:
            return node
        Q = deque([node])
        New_node = Node(node.val,[])
        clones = {node.val : New_node}
        while Q:
            curr = Q.pop()
            curr_clone = clones[curr.val]
            for neib in curr.neighbors:
                if neib.val not in clones:
                    clones[neib.val] = Node(neib.val,[])
                    Q.append(neib)
                curr_clone.neighbors.append(clones[neib.val])
        return clones[node.val]
class DFS_Solution:
    def cloneGraph(self, node):
        if not node:
            return node
        #DFS
        clones = {}
        def dfs(node):
            #visited
            if node.val in clones:
                return clones[node.val]
            #base
            clones[node.val] = Node(node.val,[])
            for neib in node.neighbors:
                clones[node.val].neighbors.append(dfs(neib))
            return clones[node.val]
        return dfs(node)
               
        
        
        
