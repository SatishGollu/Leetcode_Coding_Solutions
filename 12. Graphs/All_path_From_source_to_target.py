#k = 2^(N-2)
#TIME-O(E+k*V) 
#Space - O(N)
class DFS_Solution:
    def allPathsSourceTarget(self, graph):
        result = []
        destination = len(graph)-1
        def dfs(source,stack):
            #base
            if source == destination:
                result.append(stack.copy())
                return
            for nbrs in graph[source]:
                stack.append(nbrs)
                dfs(nbrs,stack)
                stack.pop()
        
        dfs(0,[0])
        return result

#better way of coding 
#DFS without backtracking
class Solution:
    def allPathsSourceTarget(self, graph):
        #base
        if not graph:
            return []
        #building the graph
        G = {}
        for i in range(len(graph)):
            G[i] = graph[i] # one way link
        
        #apply DFS on DAG
        n = len(graph)
        results = []
        stack = [(0,[0])]
        while stack:
            node,path = stack.pop()
            if node == n-1:
                results.append(path)
            for nbrs in G[node]:
                stack.append((nbrs,path+[nbrs]))
        return results
        
        
        