#Time    O(V+E)
#Space   O(V+E)
from collections import defaultdict,deque
class DFS_Solution:
    def isBipartite(self, graph) -> bool:
        #DFS
        color_map = {}
        def DFS(graph,node,color,color_map):
            if node in color_map:
                if color_map[node] != color:
                    return False
                return True
            color_map[node] = color
            for neighbor in graph[node]:
                if not DFS(graph,neighbor,1-color,color_map):
                    return False
            return True
        
        for each in range(len(graph)):
            if each not in color_map:
                if not DFS(graph,each,0,color_map):
                    return False
        return True
                

class BFS_Solution:
    def isBipartite(self, graph) -> bool:
        #BFS
        color_map = {}
        def BFS(node,graph,color_map):
            Q = deque([(node,0)])
            while Q:
                curr_pop,color = Q.popleft()
                if curr_pop in color_map:
                    if color_map[curr_pop] != color:
                        return False
                color_map[curr_pop] = color
                
                for neighbor in graph[curr_pop]:
                    if neighbor not in color_map:
                        Q.append((neighbor,1-color))
            return True
        
        for each in range(len(graph)):
            if each not in color_map:
                if not BFS(each,graph,color_map):
                    return False
        return True
                
            
        