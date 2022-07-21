from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #checking the number of rows
        rows = len(grid)
        #check if grid is empty
        if rows == 0:
            return -1
        #checking the number of columns
        cols = len(grid[0])

        # tracking the fresh oranges
        fresh = 0

        # deque for rotten oranges - BFS travel
        rotten = deque()

        #tracking of minutes passed
        minutes = 0

        #visiting each cell in the grid
        # and count the no. of rotten and fresh oranges
        for r in range(rows):
            for c in range(cols):
                #for rotten oranges
                if grid[r][c] == 2:
                    rotten.append((r,c))
                # for fresh oranges
                if grid[r][c] == 1:
                    fresh += 1
        #if there are rotten oranges in queue and fresh oranges then
        # loop through all
        while rotten and fresh > 0:
            minutes += 1
            for _ in range(len(rotten)):
                x,y = rotten.popleft()
                #visit all adjecent cells
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    xx, yy = x+dx, y+dy

                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    #updating the fresh count
                    fresh -= 1
                    #marking the grid to rotten
                    grid[xx][yy]=2
                    #add the cordinates to the queue
                    rotten.append((xx,yy))
        return minutes if fresh == 0 else -1















        
