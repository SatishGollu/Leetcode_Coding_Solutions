#Time - O(M*N)-we are visiting max each cell 5 times.
class DFS_Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        
        def dfs(r,c,grid):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c]!="1":
                    return
            grid[r][c] = "7"
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            for x,y in directions:
                newx,newy = x+r,y+c   
                dfs(newx,newy,grid)
        #main
        row = len(grid)
        col = len(grid[0])
        island_count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r,c,grid)
                    island_count += 1
        return island_count
                    
#Time - O(M*N)-we are visiting max each cell 5 times.
#Space-O(MN)- for dfs min(m,n) for bfs
from collections import defaultdict,deque
class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        
        
        def bfs(r,c,grid):
            if grid[r][c] != "1":
                return
            Q = deque([(r,c)])
            while Q:
                r,c = Q.popleft()
                directions = [(1,0),(0,1),(-1,0),(0,-1)]
                for i,j in directions:
                    x,y = i+r,j+c
                    if x < 0 or x >= row or y < 0 or y >= col or grid[x][y]!="1":
                        continue
                    grid[x][y] = "7"
                    Q.append((x,y))
        #main
        row = len(grid)
        col = len(grid[0])
        island_count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    bfs(r,c,grid)
                    island_count += 1
        return island_count
                    
            
                   
        