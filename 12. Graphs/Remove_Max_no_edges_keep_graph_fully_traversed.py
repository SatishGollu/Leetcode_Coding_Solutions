#Time - O(E)--number of edges
class DSUF:
    def __init__(self,N):
        self.parent = [0] * (N+1)
        self.size = [1] * (N+1)
        for i in range(N+1):
            self.parent[i] = i
            
    def find(self,i):
        if i == self.parent[i]:
            return i
        self.parent[i]= self.find(self.parent[i])
        return self.parent[i]
    def union(self,u,v):
        p1 = self.find(u)
        p2 = self.find(v)
        if p1 == p2: return 0
        if self.size[p1] < self.size[p2]:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
        else:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
        return 1
        
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges) -> int:
        
        disjoint = DSUF(n)
        result = 0
        e1 = e2 = 0
        # alice and bob traverse
        for t,i,j in edges:
            if t == 3:
                if disjoint.union(i,j):
                    e1 += 1
                    e2 += 1
                else:
                    result += 1
        parent0 = disjoint.parent.copy()
        # only alice
        for t,i,j in edges:
            if t == 1:
                if disjoint.union(i,j):
                    e1 += 1
                else:
                    result += 1
        # only bob 
        disjoint.parent = parent0
        for t,i,j in edges:
            if t == 2:
                if disjoint.union(i,j):
                    e2 += 1
                else:
                    result += 1
        return result if e1 == e2 == n-1 else -1
        
        
        
# Prims approach
import collections,heapq
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges) -> int:
		# process graph
        graphs = [collections.defaultdict(list) for _ in range(3)]
        for c, i, j in edges:
            graphs[c-1][i].append((-c, j))
            graphs[c-1][j].append((-c, i))
		# build tree for Alice
        e = graphs[2][1] + graphs[0][1]
        heapq.heapify(e)
        treeset = set([1])
        type3 = 0
        while e:
            c, y = heapq.heappop(e)
            if y not in treeset:
                treeset.add(y)
                if c == -3:
                    type3 += 1
                for item in graphs[2][y]:
                    heapq.heappush(e, item)
                for item in graphs[0][y]:
                    heapq.heappush(e, item)
        if len(treeset) != n:
            return -1
		# build tree for Bob
        e = graphs[2][1] + graphs[1][1]
        heapq.heapify(e)
        treeset = set([1])
        while e:
            c, y = heapq.heappop(e)
            if y not in treeset:
                treeset.add(y)
                for item in graphs[2][y]:
                    heapq.heappush(e, item)
                for item in graphs[1][y]:
                    heapq.heappush(e, item)
        if len(treeset) != n:
            return -1
        return len(edges) + type3 - 2 * (n - 1)      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        