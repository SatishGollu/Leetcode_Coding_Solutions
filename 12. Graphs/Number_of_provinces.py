class dfs_Solution:
    def findCircleNum(self, isConnected) -> int:
        visited = set()
        N = len(isConnected)
        #dfs function
        def dfs(node):
            for neighbor,adjecent in enumerate(isConnected[node]):
                if adjecent == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        result = 0
        for i in range(N):
            if i in visited:
                continue
            dfs(i)
            result += 1
        return result
#using disjoint set
class dsuf:
    
    def __init__(self,n):
        self.parent = [i for i in range(n)]
    
    def find(self,i):
        if i == self.parent[i]:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu != pv:
            self.parent[pv] = pu   
class Solution:
    def findCircleNum(self, isConnected) -> int:
        if not isConnected: return 0
        N = len(isConnected)
        unionfind = dsuf(N)
        for i in range(N):
            for j in range(i,N):
                if isConnected[i][j] == 1:
                    unionfind.union(i,j)
        result = 0
        for x in range(N):
            if unionfind.parent[x] == x:
                result += 1
        print(unionfind.parent)
        return result

