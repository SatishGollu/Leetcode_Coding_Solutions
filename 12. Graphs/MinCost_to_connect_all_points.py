#Time - O(nlogn) but solution is dominated by O(n*n) because of graph creation
from collections import defaultdict
from heapq import heappop,heappush
class Solution:
    def minCostConnectPoints(self, points) -> int:
        #using prims algo
        graph = defaultdict(list)
        n = len(points)
        #building graph
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                distance = abs(x1-x2) + abs(y1-y2)
                graph[i].append((distance,j))
                graph[j].append((distance,i))
                
        #bfs
        answer = 0
        visited = set()
        Q = [(0,0)] #--(cost,point)
        while len(visited) < n:
            cost,i = heappop(Q)
            if i in visited: continue
            answer += cost
            visited.add(i)
            for nbr_cost,nbr in graph[i]:
                if nbr not in visited:
                    heappush(Q,(nbr_cost,nbr))
        return answer
            
        
        