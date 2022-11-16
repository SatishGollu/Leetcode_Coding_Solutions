# BFS
#TIME- O(M*N)--SPACE O(N)
from collections import defaultdict,deque
class BFS_Solution:
    def calcEquation(self, equations, values, queries):
        # using BFS
        #creating adjecent Graph
        Graph = defaultdict(dict)
        for (x,y),v in zip(equations,values):
            Graph[x][y] = v
            Graph[y][x] = 1/v
        
        def BFS(source,destination):
            if not (source in Graph and destination in Graph):
                return -1.0
            Q = [(source,1)]
            seen = set()
            for x,v in Q:
                if x == destination:
                    return v
                seen.add(x)
                for neighbors in Graph[x]:
                    if neighbors not in seen:
                        Q.append((neighbors, v*Graph[x][neighbors]))
            return -1.0
        result = []
        for s,d in queries:
            ans = BFS(s,d)
            result.append(ans)
        return result
            
        
