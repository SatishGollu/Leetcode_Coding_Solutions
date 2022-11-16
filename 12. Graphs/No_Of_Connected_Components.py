#1. Naive union find
#TIME-O(E*V) E-- edges and v for nodes
class Solution:
    def countComponents(self, n: int, edges) -> int:
        def find(parent,i):
            while (i != parent[i]):
                i = parent[i]
            return i
        #naive union find
        parent = [-1]*n
        components = n
        for x,y in edges:
            p1 = find(parent,x)
            p2 = find(parent,y)
            if (p1 != p2):
                parent[p1] = p2
                components -= 1
        return components

#2Time: O(n+mlogn), where m is the number of connections, n is the number of nodes.
#By doing Path Compression, it has been proven to achieve in O(logN) in each operations.
#Space: O(n)
class Solution:
    # using path compression
    def countComponents(self, n: int, edges) -> int:   
        def find(parent,i):
            if (i == parent[i]):
                return i
            parent[i] = find(parent,parent[i]) #path compression
            return parent[i]
        
        parent = [i for i in range(n)]
        components = n
        for x,y in edges:
            p1 = find(parent,x)
            p2 = find(parent,y)
            if (p1 != p2):
                parent[p1] = p2
                components -= 1
        return components

#3. optimized one
#Time: O(n + m*α(n)) ≈ O(n + m), where m is the number of 
# connections (union operations), n is the number of nodes.
#according to ackermann function α(n) < 5. 
#Space - O(n)
class solution:
    def countComponents(n,edges):
        parent = []
        size = []
        components = n
        for i in range(n):
            parent[i] = i
            size[i] = 1
        def find(parent,i):
            if (i == parent[i]):
                return i
            parent[i] = find(parent,parent[i]) #path compression
            return parent[i]
        
        for x,y in edges:
            p1 = find(parent,x)
            p2 = find(parent,y)

            if (p1 != p2):
                if size[p1] < size[p2]:
                    size[p2] += size[p1]
                    parent[p1] = p2
                else:
                    size[p1] += size[p2]
                    parent[p2] = p1
                components -= 1
        return components

#4 using DFS
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges) -> int:
        Graph = defaultdict(list)
        visited = [0]*n
        components = 0
        for x,y in edges:
            Graph[x].append(y)
            Graph[y].append(x)
        #dfs funtion
        def dfs(i,Graph,visited):
            #base
            if visited[i]:
                return 
            visited[i] = 1
            for neighbor in Graph[i]:
                dfs(neighbor,Graph,visited)
        for i in range(n):
            if not visited[i]:
                #dfs function
                dfs(i,Graph,visited)
                components += 1
        return components
                
