from collections import defaultdict,deque
from unittest import result
class Depth_Frist_solution:
    def findorder(self,N,Prerequisites):
        Graph = defaultdict(list)
        indegree = [0]*N
        result = []
        #creating adjeceny graph
        for pre,nxt in Prerequisites:
            Graph[pre].append(nxt)
            indegree[nxt] += 1
        #function for dfs traversel
        def dfs(curr):
            result.append(curr)
            indegree[curr] = -1
            for nextval in Graph[curr]:
                indegree[nextval] -= 1
                if indegree[nextval] == 0:
                    dfs(nextval)

        for i in range(N):
            if indegree[i] == 0:
                #then dfs
                dfs(i)
        return result if len(result) == N else []
class Bredth_Frist_solution:
    def findorder(self,N,Prerequisites):
        Graph = defaultdict(list)
        indegree = [0]*N
        Q = deque()
        result = []
        #creating adjeceny graph
        for pre,nxt in Prerequisites:
            Graph[pre].append(nxt)
            indegree[nxt] += 1
        #bfs traversel
        for i in range(N):
            if indegree[i] == 0:
                Q.append(i)
        while Q:
            curr = Q.popleft()
            result.append(curr)
            for nxt in Graph[curr]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    Q.append(nxt)
        return result if len(result) == N else []

if __name__ == "__main__":
    lis = [[5,0],[5,2],[2,3],[3,1],[4,0],[4,1]]
    compute = Depth_Frist_solution()
    result = compute.findorder(len(lis),lis)
    print(result)