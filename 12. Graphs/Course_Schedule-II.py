from collections import defaultdict,deque
class DFS_Solution:
    def findOrder(self, numCourses: int, prerequisites):
        # dfs method
        Graph = defaultdict(list)
        indegree = [0] * numCourses
        result = []
        
        # forming the adjacency list of graph and indegree list
        for nxt,pre in prerequisites:
            Graph[pre].append(nxt)
            indegree[nxt] += 1
        #function to make dfs traversal
        def dfs(curr):
            result.append(curr)
            #mark the visited
            indegree[curr] = -1
            for next_course in Graph[curr]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    dfs(next_course)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
        
        return result if len(result) == numCourses else []

"""
Time Complexity : O(N + E), We require O(E) to form 
adjacency list and O(N + E) for standard DFS traversal.
Space Complexity : O(N + E), required for recursive stack 
and storing prerequisites as adjacency list graph in G
"""
# kahn's algorithm
class BFS_Solution:
    from collections import defaultdict,deque
    def findOrder(self, numCourses: int, prerequisites):
        # bfs method
        Graph = defaultdict(list)
        indegree = [0] * numCourses
        Q = deque()
        result = []
        
        # forming the adjacency list of graph and indegree list
        for nxt,pre in prerequisites:
            Graph[pre].append(nxt)
            indegree[nxt] += 1
        #bfs traversel
        for i in range(numCourses):
            if indegree[i] == 0:
                Q.append(i)
        while Q:
            curr = Q.popleft()
            result.append(curr)
            for next_course in Graph[curr]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    Q.append(next_course)
        
        return result if len(result) == numCourses else []
"""
Time Complexity : O(N + E), where N is the number of courses and 
E is the number of edges, i.e, P_length. We require O(E) to form
adjacency list and O(N + E) for standard BFS traversal.
Space Complexity : O(N + E), required for queue and storing 
prerequisites as adjacency list graph in G

"""