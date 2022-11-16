from collections import defaultdict,deque
import math
class BFS_Solution:
    def maximumDetonation(self, bombs) -> int:
        #bfs
        graph = defaultdict(list)
        n = len(bombs)
        #step - 1 building the graph from bombs
        for i,(xi,yi,ri) in enumerate(bombs):
            for j,(xj,yj,rj) in enumerate(bombs):
                if i == j: continue
                distance = math.sqrt((xj-xi)**2 + (yj-yi)**2)
                if distance <= ri:
                    graph[i].append(j)
                if distance <= rj:
                    graph[j].append(i)
        #BFs function
        def bfs(node):
            Q = deque([node])
            visited = set([node])

            while Q:
                detonate = Q.popleft()
                for nbrs in graph[detonate]:
                    if nbrs not in visited:
                        visited.add(nbrs)
                        Q.append(nbrs)
            return len(visited)
        #main
        max_bombs = 0
        for i in range(n):
            curr_ans = bfs(i)
            max_bombs = max(max_bombs,curr_ans)
        return max_bombs

                
#DFS
from collections import defaultdict,deque
import math
class Solution:
    def maximumDetonation(self, bombs) -> int:
        #bfs
        graph = defaultdict(list)
        n = len(bombs)
        #step - 1 building the graph from bombs
        for i,(xi,yi,ri) in enumerate(bombs):
            for j,(xj,yj,rj) in enumerate(bombs):
                if i == j: continue
                distance = math.sqrt((xj-xi)**2 + (yj-yi)**2)
                if distance <= ri:
                    graph[i].append(j)
                if distance <= rj:
                    graph[j].append(i)
        #dFs function
        def dfs(node):
            for nbrs in graph[node]:
                if nbrs not in visited:
                    visited.add(nbrs)
                    dfs(nbrs)
            return len(visited)
        #main
        max_bombs = 0
        for i in range(n):
            visited = set([i])
            curr_ans = dfs(i)
            max_bombs = max(max_bombs,curr_ans)
        return max_bombs

                




