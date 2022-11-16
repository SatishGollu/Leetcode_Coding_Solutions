#greedy TIMe- O(n2)
class Solution:
    def minSwapsCouples(self, row) -> int:
        answer = 0
        for i in range(0,len(row),2):
            x = row[i]
            if row[i+1] == x^1:
                continue
            answer += 1
            for j in range(i+1,len(row)):
                if row[j] == x^1:
                    row[i+1],row[j] = row[j],row[i+1]
                    break
        return answer
# Optimized one with my solution using union find
# Time-O(logn)
# space - O(n)
class unionfind:
    def __init__(self,N):
        self.parent = [0] * N
        self.size = [0] * N
    def find(self,i):
        if i == self.parent[i]:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu==pv:
            return 0
        else:
            if self.size[pu] < self.size[pv]:
                self.parent[pu] = pv
                self.size[pv] += self.size[pu]
            else:
                self.size[pu] += self.size[pv]
                self.parent[pv] = pu
            return 1
class Solution:
    def minSwapsCouples(self, row) -> int:
        swaps = 0
        N = len(row)
        dsuf = unionfind(N)
        for i in range(0,N,2):
            dsuf.parent[row[i]] = row[i]
            dsuf.parent[row[i+1]]= row[i]
        #swaps 
        for i in range(0,N,2):
            swaps += dsuf.union(i,i+1)
        return swaps       