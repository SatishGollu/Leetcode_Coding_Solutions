# modifying grid or using set upto you, depends on interviewr
#but modifying will save O(M*N) space
# modifying grid or using set upto you, depends on interviewr
#but modifying will save O(M*N) space
from collections import defaultdict,deque
class Solution:
    def getFood(self, grid) -> int:
        
        #BFS
        m = len(grid)
        n = len(grid[0])
        Q = deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        #finding the locaiton
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "*":
                    Q.append((r,c,0))
                    break
    
        #main
        while Q:
            r,c,path = Q.popleft()
            
            for x,y in directions:
                newr = x+r
                newc = y+c
                if 0 <= newr < m and 0 <= newc < n and grid[newr][newc] in ("#","O"):
                    
                    if grid[newr][newc] == "#":
                        return path+1
                    
                    grid[newr][newc]="7"
                    Q.append((newr,newc,path+1))
                    
        return -1
            
            
            
                    
        