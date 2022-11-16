from collections import defaultdict
from heapq import heappop,heappush
#TIME- O(v+eloge)
class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        graph = defaultdict(list)
        #building adjacency list
        for (u,v),p in zip(edges,succProb):
            graph[u].append((v,p))
            graph[v].append((u,p))
        visited = set()
        #bfs
        Q = [(-1,start)]
        while Q:
            prob, node = heappop(Q)
            if node == end:
                return -prob
            if node in visited: continue
            visited.add(node)
            for nbr,weight in graph[node]:
                if nbr in visited: continue
                new_prob = prob * weight
                heappush(Q,(new_prob,nbr))
        return 0

        
        