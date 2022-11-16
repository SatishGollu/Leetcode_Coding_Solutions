import sys
class Solution:
    def minTrioDegree(self, n: int, edges) -> int:
        adj_matrix = [[0]*(n+1) for _ in range(n+1)]
        indegree = {c:0 for c in range(n+1)}
        min_degree = sys.maxsize
        for u,v in edges:
            adj_matrix[u][v] = 1
            adj_matrix[v][u] = 1

            indegree[v] += 1
            indegree[u] += 1
        #main
        for i in range(n+1):
            for j in range(i+1,n+1):
                if not adj_matrix[i][j]: continue
                for k in range(j+1,n+1):
                    if adj_matrix[i][j] == 1 and adj_matrix[j][k] == 1 and adj_matrix[k][i] ==1:
                        curr_degree = indegree[i]+indegree[j]+indegree[k]-6
                        #because of undirected there always be 2 extra edges from a node
                        min_degree = min(min_degree,curr_degree)
        return -1 if min_degree == sys.maxsize else min_degree
