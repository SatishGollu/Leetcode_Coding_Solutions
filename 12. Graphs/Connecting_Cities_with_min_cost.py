from collections import defaultdict
from heapq import heappush,heappop
class Prims_Solution:
    def minimumCost(self, n: int, connections) -> int:
        if not connections:
            return 0
        #list of list for adjacency graph
        Graph = defaultdict(list)
        # visited set
        visited = set()
        # parent: child map with costs--(key-parent,child, value-cost)
        # no need for this problem but in general to keep track of what nodes.
        min_cost_cities = {(n,n):0}
        # variable for total minimum cost
        total = 0
        # Queue
        Q = [(0,(n,n))] #--- random element to start with queue
        #building adjaceny list
        for u,v,cost in connections:
            Graph[u].append((v,cost))
            Graph[v].append((u,cost))
        #main
        while Q and len(visited) <= n:
            cost,pop_ele = heappop(Q)
            parent,node = pop_ele
            if node not in visited:
                visited.add(node)
                total = total+cost
                min_cost_cities[(parent,node)] = cost
                for nbr_node,cost in Graph[node]:
                    heappush(Q,(cost,(node,nbr_node)))
        return total if len(visited) == n else -1
        
# Time - O(Elogv)


class DSUF():
    def __init__(self):
        self.parent = {}
        self.size = {}
    def set_node(self,key):
        self.parent[key] = key
        self.size[key] = 1
    def find(self,i):
        #base
        if i == self.parent[i]:
            return i
        self.parent[i] = self.find(self.parent[i])#path compression
        return self.parent[i]
    def union(self,u,v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        
        if parent_u != parent_v:
            if self.size[parent_u] < self.size[parent_v]:
                self.size[parent_v] += self.size[parent_u]
                self.parent[parent_u] = parent_v
            else:
                self.size[parent_u] += self.size[parent_v]
                self.parent[parent_v] = parent_u
            return True
        return False

# Time - O(ElogV)
# space - O(N)
class Kruskal_Solution:
    def minimumCost(self, n: int, connections) -> int:
        #sorting the components
        connections.sort(key = lambda connection: connection[2])
        dsuf = DSUF()
        for node in range(n+1):
            dsuf.set_node(node)
        components = n
        total_cost = 0
        for u,v,cost in connections:
            if dsuf.union(u,v):
                components -= 1
                total_cost += cost
                if components == 1:
                    break
        return total_cost if components == 1 else -1
            
            
            
        