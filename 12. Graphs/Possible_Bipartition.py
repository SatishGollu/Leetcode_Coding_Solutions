from collections import defaultdict,deque
#DFS
class Solution:
    def possibleBipartition(self, n: int, dislikes) -> bool:
        graph = defaultdict(list)
        color_map = {}
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(start,color):
            if start in color_map and color_map[start] != color:
                return False
            if start not in color_map:
                color_map[start] = color
                for nbrs in graph[start]:
                    #if nbrs not in color_map:
                    if not dfs(nbrs,1-color):
                        return False
            return True
        
        for i in range(1,n+1):
            if i not in color_map:
                if not dfs(i,0):
                    return False
        return True

class BFS_Solution:
    def possibleBipartition(self, n: int, dislikes) -> bool:
        #BFS
        Graph = defaultdict(list)
        color_map = {}
        for node,adj_node in dislikes:
            Graph[node].append(adj_node)
            Graph[adj_node].append(node)
        def BFS(start):
            Q = [(start,0)]
            while Q:   
                curr_node,color = Q.pop()
                if curr_node in color_map:
                    if color_map[curr_node] != color:
                        return False
                color_map[curr_node] = color
                #neighbors
                for vertice in Graph[curr_node]:
                    if vertice not in color_map:
                        Q.append((vertice,1-color))
            return True
        # main
        for i in range(n):
            if i not in color_map:
                 if not BFS(i):
                        return False
        return True