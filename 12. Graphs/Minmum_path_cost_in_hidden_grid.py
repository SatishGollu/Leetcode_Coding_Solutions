# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> int:
#        
#
#    def isTarget(self) -> None:
#        
#
from collections import defaultdict,deque
from heapq import heappush,heappop
import sys
class Solution(object):
    def findShortestPath(self, master) -> int:
        directions = {"U":(-1,0),"D":(1,0),"L":(0,-1),"R":(0,1)}
        reverse = {"U":"D","D":"U","L":"R","R":"L"}
        cost_dict = defaultdict(lambda:sys.maxsize)
        target = None
        
        #dfs function to recored valid grid locations
        def dfs(master,r,c):
            nonlocal target
            if master.isTarget():
                target = r,c
                return True
            ans = False
            for d in directions:
                x,y = directions[d]
                newr,newc = r+x,c+y 
                if (newr,newc) in cost_dict:continue
                cost_dict[(newr,newc)] = sys.maxsize
                if master.canMove(d):
                    cost = master.move(d)
                    cost_dict[(newr,newc)] = cost
                    ans |= dfs(master,newr,newc)
                    master.move(reverse[d])
            return ans
        #calling dfs
        if not dfs(master,0,0):return -1
        #starting a BFS call from here 
        
        Q_heap = [(0,0,0)] #-- cost,row,col
        while Q_heap:
            cost,r,c = heappop(Q_heap)
            if (r,c) == target:
                return cost
            for d in directions:
                x,y = directions[d]
                newr,newc = x+r,y+c
                if (newr,newc) not in cost_dict: continue
                heappush(Q_heap,(cost+cost_dict[(newr,newc)] , newr,newc))
                cost_dict[(newr,newc)] = sys.maxsize
        return -1
                

































