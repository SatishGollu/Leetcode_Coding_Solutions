#BFS-iteration --TLE
#TIMe - O(m*n*k)---k is the max cur_score that need to traverse
#Space - O(m*n)
from collections import defaultdict,deque
class BFS_iteration_Solution:
    def maximumMinimumPath(self, grid) -> int:
        #BFS- iteration
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        # bfs function
        
        def path_exists(cur_score):
            visited = set((0,0))
            Q = deque([(0,0)])
            while Q:
                row,col = Q.popleft()
                #base
                if row == m-1 and col == n-1:
                    return True
                for x,y in directions:
                    nrow,ncol = x+row,y+col
                    if 0 <= nrow < m and 0 <= ncol < n and (nrow,ncol) not in visited:
                        if grid[nrow][ncol] >= cur_score:
                            visited.add((nrow,ncol))
                            Q.append((nrow,ncol))
            return False
        cur_score = min(grid[0][0],grid[m-1][n-1])
        #start a cur_score, check if we can find a path of score equal to cur_score
        while cur_score >= 0:
            if path_exists(cur_score):
                return cur_score
            else:
                cur_score -= 1
                
#BFS-Binary search
#TIme - O(M*N*logk)
class BFS_Binary_search_Solution:
    def maximumMinimumPath(self, grid) -> int:
        #BFS- Binarysearch
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        # bfs function
        
        def path_exists(cur_score):
            visited = set((0,0))
            Q = deque([(0,0)])
            while Q:
                row,col = Q.popleft()
                #base
                if row == m-1 and col == n-1:
                    return True
                for x,y in directions:
                    nrow,ncol = x+row,y+col
                    if 0 <= nrow < m and 0 <= ncol < n and (nrow,ncol) not in visited:
                        if grid[nrow][ncol] >= cur_score:
                            visited.add((nrow,ncol))
                            Q.append((nrow,ncol))
            return False
        
        left = 0
        right = min(grid[0][0],grid[m-1][n-1])
        #start a cur_score, check if we can find a path of score equal to cur_score
        while left < right:
            mid = (left + right+1) >> 1
            if path_exists(mid):
                left = mid
            else:
                right = mid-1
        return left
                
 #dFS-Binary search
class DFS_Binary_Solution:
    def maximumMinimumPath(self, grid) -> int:
        #dFS- Binarysearch
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        # dfs function
        
        def path_exists(cur_score):
            visited = set((0,0))
            def dfs(row,col):
                #base
                if row == m-1 and col == n-1:
                    return True
                visited.add((row,col))
                for x,y in directions:
                    nrow,ncol = x+row,y+col
                    if 0 <= nrow < m and 0 <= ncol < n and (nrow,ncol) not in visited:
                        if grid[nrow][ncol] >= cur_score and dfs(nrow,ncol):
                            return True
                return False
            return dfs(0,0)
        
        left = 0
        right = min(grid[0][0],grid[m-1][n-1])
        #start a cur_score, check if we can find a path of score equal to cur_score
        while left < right:
            mid = (left + right+1) >> 1
            
            if path_exists(mid):
                left = mid
            else:
                right = mid-1
        return left
                
#BFS-Queue ----~~ Dijkstra
#Time -- O(M*N*log(m*n))
from heapq import heappush,heappop
class Solution:
    def maximumMinimumPath(self, grid) -> int:
        
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set((0,0))
        result = grid[0][0]
        Q = [(-grid[0][0],0,0)]
        while Q:
            value,row,col = heappop(Q)
            #update the min value we have visited so far
            result = min(result,grid[row][col])
            # if we reach bottom then break
            if row == m-1 and col == n-1:
                break
            for x,y in directions:
                nrow,ncol = x+row,y+col
                if 0 <= nrow < m and 0 <= ncol < n and (nrow,ncol) not in visited:
                    heappush(Q,(-grid[nrow][ncol],nrow,ncol))
                    visited.add((nrow,ncol))
        return result
    
            
                  
                   
                   
        