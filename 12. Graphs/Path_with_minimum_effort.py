# TIME - O(ElogV)
# SPACE - O(E+V)
class DIJKSTRA_Solution:
    def minimumEffortPath(self, heights):
        #using dijkstra
        grid = heights
        if not grid:
            return 0
        from heapq import heappush, heappop
        import math
        hp = [(0,(0,0))]#cost is key for heap
        cost_so_far = {(0,0):0} # also serves as a more nuanced visited set
        # cameFrom = {(0,0): None} # (child : parent) Only required for path finding 
        target = (len(grid)-1,len(grid[0])-1) # dijkstra can have early stopping
        while hp:
            cost,node = heappop(hp)
            x,y = node
            
            if node == target:
                break
            # for all 4 directions
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            
            for direction in directions:
                newx,newy = x+direction[0],y+direction[1]
                #boundries 
                if newx >= 0 and newx <= len(grid)-1 and newy >= 0 and newy <= len(grid[0])-1:
                    edgecost = max(cost,abs(grid[x][y] - grid[newx][newy]))
                    # if nei not seen before or seen before but now revisiting via less costly route
                    if (newx,newy) not in cost_so_far or ((newx,newy) in cost_so_far and edgecost < cost_so_far[(newx,newy)]):
                        cost_so_far[(newx,newy)] = edgecost
                        heappush(hp,(edgecost,(newx,newy)))
        #print(cost_so_far)                
        return cost_so_far[target]
                
# Time: O(M * N * log(MAX_HEIGHT)), where MAX_HEIGHT = 10^6, 
# M <= 100 is the number of rows and N <= 100 is the number of columns in the matrix.
# Space: O(M * N)

class DFS_Solution:
    def minimumEffortPath(self, heights):
        grid = heights
        if not grid:
            return 0
        # function
        def dfs(r,c,mid,visited):
            #base
            if r == row-1 and c == col-1:   
                return True
            visited[r][c] = True
            # for all 4 directions
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            for x,y in directions:
                newx,newy = r+x,c+y
                #boundries 
                if (0 <= newx <= row-1) and (0<= newy <= col-1) and not visited[newx][newy]:

                    edgecost = abs(grid[r][c] - grid[newx][newy])
                    if edgecost <= mid and dfs(newx,newy,mid,visited):
                        return True
            return False
        #funtion
        def canreach_Destination(mid):
            visited = [[False]*col for _ in range(row)]
            return dfs(0,0,mid,visited)
                
        # Main
        row = len(grid)
        col = len(grid[0])
        left = 0
        right = 10**6+1
        while left < right:
            mid = (left + right) >> 1
            if canreach_Destination(mid):
                right = mid
            else:
                left = mid + 1
        return left
                
            
    