class dsuf:
    
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
    
    def find(self,i):
        if i == self.parent[i]:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        self.parent[pv] = pu
        return True
                       
class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        dsu = dsuf(n)
        result = []
        for u,v in edges:
            if dsu.union(u,v):
                continue
            result.append([u,v])
        return result[-1]
           