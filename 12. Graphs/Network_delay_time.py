from collections import defaultdict,deque
from heapq import heappop,heappush
# time - O(Elogv)
class Dijkstra_Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        #dijkstra
        if not times:
            return 0
        # adjacency list
        graph = defaultdict(list)
        distance = [0] + [float("inf")] * n
        visited = set()
        #building graph
        for src,dst,c in times:
            graph[src].append((c,dst))
        #
        Q = [(0,k)]#---(cost,node)
        while Q:
            cost,node = heappop(Q)
            if cost < distance[node]:
                distance[node] = cost
            if node not in visited:
                visited.add(node)
                for weight,new_node in graph[node]:
                    heappush(Q,((cost + weight),new_node))
        
        max_cost = max(distance)
        
        return max_cost if max_cost < float('inf') else -1


class Bellman_Solution:
    #time O(Ev)
    #space O(e+v)
    def networkDelayTime(self, times, n: int, k: int) -> int:
        distance = [0]+[float('inf')]*n
        distance[k] = 0
        for _ in range(n-1):
            stop = 1
            for u,v,w in times:
                if distance[u]+w < distance[v]:
                    distance[v] = distance[u]+w
                    stop = 0
            if stop:
                break
        max_c = max(distance)
        return max_c if max_c < float('inf') else -1