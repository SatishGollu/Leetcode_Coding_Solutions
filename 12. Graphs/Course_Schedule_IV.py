from collections import defaultdict,deque
#Time Complexity: O((V+E) * V) = O(V^3) in the worst case, 
# but actually runs faster in practice
#Space Complexity: O(V^2)
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites,queries) :
        #topological sorting and look up dictionary
        graph = defaultdict(list)
        indegree = defaultdict(int)
        pre_courses = defaultdict(set)

        #creating graph and counting indegree
        for pre,post in prerequisites:
            graph[pre].append(post)
            indegree[post] += 1
        #add 0- degrees nodes to the Q
        Q = deque([])
        for n in graph:
            if indegree[n] == 0:
                Q.append(n)
        # use BFS to do topological sort to create a prerequisite lookup dictionary
        while Q:
            cur = Q.popleft()
            for neighbor in graph[cur]:
                pre_courses[neighbor].add(cur)  
                pre_courses[neighbor].update(pre_courses[cur])
                
                indegree[neighbor] -= 1         # regular topological search operations
                if indegree[neighbor] == 0:
                    Q.append(neighbor)
        #traverse the Queires and return results
        result = []
        for u,v in queries:
            if u in pre_courses[v]:
                result.append(True)
            else:
                result.append(False)
        return result
                

#
from collections import defaultdict,deque
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites, queries) :
        #floyd warshall
        connected = [[False]*n for i in range(n)]

        for u,v in prerequisites:
            connected[u][v] = True
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    connected[i][j] = connected[i][j] or (connected[i][k] and connected[k][j])

        # queires
        return [connected[i][j] for i,j in queries]
#Time-O(v3)
#Space - O(v2)











