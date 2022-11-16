from collections import defaultdict, deque
from heapq import heappop,heappush
#Time- O(k*ElogV)
#space - O(V+E)
class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, K: int) -> int:
        #dijkstra
        graph = defaultdict(list)
        heap = [(0,src,K+1)]
        visited = [0]*n

        # creating adjacency list 
        for source,destinaiton,cost in flights:
            graph[source].append((destinaiton,cost))
        
        #main BFS
        while heap:
            cost,node,k = heappop(heap)
            if node == dst:
                return cost
            if visited[node] >= k:
                continue
            visited[node] = k
            for new_node,price in graph[node]:
                heappush(heap,(cost+price,new_node,k-1))
        return -1
#bellman-ford
#time - O(k*E)
#Space - O(v)
class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, K: int) -> int:
        #bellman-ford
        prices = [float('inf')]*n
        prices[src] = 0
        for i in range(K+1):
            temp = prices.copy()
            for s,d,cost in flights:
                if prices[s] == float('inf'): continue
                if prices[s]+cost < temp[d]:
                    temp[d] = prices[s]+cost
            prices = temp
        return -1 if prices[dst] == float('inf') else prices[dst]
            