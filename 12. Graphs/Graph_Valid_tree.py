from collections import defaultdict,deque
# a graph must have n-1 edges to become a tree and 
#should have 1 component i.e one root
# Time - O(N+N-1) -- O(N)
#Space - O(N)
class Solution:
    def validTree(self, n: int, edges):
        #BFS
        if len(edges) != n-1:
            return False
        #building adjacency list
        Graph = defaultdict(list)
        for u,v in edges:
            Graph[u].append(v)
            Graph[v].append(u)
        #main    
        Q = deque([0])
        visited = {0}
        while Q:
            node = Q.popleft()
            for nbrs in Graph[node]:
                if nbrs not in visited:
                    Q.append(nbrs)
                    visited.add(nbrs)
        return len(visited) == n
class Solution:
    def validTree(self, n: int, edges) -> bool:
        if len(edges) != n-1:
            return False
        #building adjacency list
        Graph = defaultdict(list)
        for u,v in edges:
            Graph[u].append(v)
            Graph[v].append(u)
        visited = set()
        #dfs
        def dfs(node):
            visited.add(node)
            for nbrs in Graph[node]:
                if nbrs not in visited:
                    dfs(nbrs)
        dfs(0)
        return len(visited) == n
            
# Time Complexity : O(N⋅α(N))
# Space : O(N)
class Union_Find_Solution:
    def validTree(self, n: int, edges) -> bool:
        if len(edges) != n-1:
            return False
        parent = []
        size = []
        for i in range(n):
            parent.append(i)
            size.append(1)
        def find(parent,i):
            if i == parent[i]:
                return i
            parent[i] = find(parent,parent[i])
            return parent[i]
        
        def union(u,v):
            p1 = find(parent,u)
            p2 = find(parent,v)
            # base
            if p1 == p2:
                return False
            if size[p1] < size[p2]:
                size[p2] += size[p1]
                parent[p1] = p2
            else:
                size[p1] += size[p2]
                parent[p2] = p1
            return True
        components = n
        for u,v in edges:
            if not union(u,v):
                return False
            components -= 1
        return components == 1

