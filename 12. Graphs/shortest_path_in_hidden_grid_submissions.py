            
# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#
from collections import defaultdict,deque
from heapq import heappop,heappush
class Solution(object):
    def findShortestPath(self, master) -> int:
        
        #usind dfs to find all the possible positions that can be reached
        directions = {"U":(-1,0),"D":(1,0),"L":(0,-1),"R":(0,1)}
        reverse = {"U":"D","D":"U","L":"R","R":"L"}
        
        isvalid = set([(0,0)])
        target = None
        
        def dfs(master,r,c):
            nonlocal target
            if master.isTarget():
                target = r,c
                return True
            ans = False
            for d in directions:
                nr,nc = directions[d]
                newr,newc = r+nr,c+nc
                if (newr,newc) not in isvalid and master.canMove(d):
                    master.move(d)
                    isvalid.add((newr,newc))
                    ans |= dfs(master,newr,newc)
                    #move back to the position before dfs
                    master.move(reverse[d])
            return ans
        # making dfs call
        if not dfs(master,0,0): return -1
        #now make the bfs to find minimum distance
        Q = deque([(0,0,0)])#--(step,row,col)
        dires = [(1,0),(0,1),(-1,0),(0,-1)]
        while Q:
            step,r,c = Q.popleft()
            if (r,c) == target: return step
            for x,y in dires:
                nr,nc = x+r,y+c
                if(nr,nc) not in isvalid: 
                    continue
                Q.append((step+1,nr,nc))
                isvalid.remove((nr,nc))           
        return -1
            
                
        
                
        
