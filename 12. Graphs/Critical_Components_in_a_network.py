#Time - O(v+e)
#space - O(e)
from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections) :
        #dfs function
        def dfs(u,discovery_rank):
            #base
            if ranks[u]:
                return ranks[u]
            ranks[u] = discovery_rank
            min_rank = discovery_rank + 1
            for v in graph[u]:
                if not ranks[v] or ranks[v] != discovery_rank-1:
                    recursive_rank = dfs(v,discovery_rank+1)
                    if recursive_rank <= discovery_rank:
                        conn_dict.remove((min(u,v),max(u,v)))
                    min_rank = min(min_rank,recursive_rank)
            return min_rank
        graph = defaultdict(list)
        ranks = [None] * n #----default rank for univisited nodes is null
        conn_dict = set()
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
            conn_dict.add((min(u,v),max(u,v)))
        
        dfs(0,0)
        return list(conn_dict)

from collections import defaultdict
class Tarjans_Solution:
    def criticalConnections(self, n: int, connections):
        graph = defaultdict(list)
        disc = [0]*n
        low = [0]*n
        time = 1
        ans = []
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(curr,prev):
            nonlocal time
            disc[curr] = low[curr] = time
            time += 1
            for nxt in graph[curr]:
                if not disc[nxt]:
                    dfs(nxt,curr)
                    low[curr] = min(low[curr],low[nxt])
                elif nxt != prev:
                    low[curr] = min(low[curr],disc[nxt])
                if low[nxt] > disc[curr]:
                    ans.append([curr,nxt])
        dfs(0,-1)
        return ans

        

        
          

        
        