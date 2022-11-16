# TIme --- O(N+E)
#Space ---O(N+E)
from collections import defaultdict,deque
class Solution:
    def minimumSemesters(self, n, relations):
        if not n:
            return -1
        #kahn's algorithm
        graph = defaultdict(list)
        indegree = [0]*(n+1)
        Q = deque()
        for pre,nxt in relations: #---O(N+E)
            graph[pre].append(nxt)
            indegree[nxt] += 1
        for i in range(1,len(indegree)):
            if indegree[i] == 0:
                Q.append((i,1))
        visited = set()
        semesters = 1
        while Q:
            node,semester = Q.popleft()
            semesters = max(semester,semesters)
            if node in visited: continue 
            visited.add(node)
            for nbrs in graph[node]:
                indegree[nbrs] -= 1
                if indegree[nbrs] == 0:
                    Q.append((nbrs,semester+1))
        
        return semesters if n == len(visited) else -1