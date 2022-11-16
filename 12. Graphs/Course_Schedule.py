from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # Bfs method
        Graph = defaultdict(list)
        indegree = [0] * numCourses
        Q = []
        
        # forming the adjacency list of graph and indegree list
        for nxt,pre in prerequisites:
            Graph[pre].append(nxt)
            indegree[nxt] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                Q.append(i)
                
        for course in Q:
            for neighbour in Graph[course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    Q.append(neighbour)
        return len(Q) == numCourses