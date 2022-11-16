# by expanding current size to 3x3 matrix, it's simply count the number of islands problem
#Upscaled grid
class DFS_Solution:
    def regionsBySlashes(self, grid) -> int:
        #lengths
        m,n = len(grid),len(grid[0])
        #list of list to convert to 3x3 matrix
        matrix = [[0] * (m*3) for i in range(n*3)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="/":
                    matrix[i*3][j*3+2] = 1
                    matrix[i*3+1][j*3+1] = 1
                    matrix[i*3+2][j*3] = 1
                elif grid[i][j]=="\\":
                    matrix[i*3][j*3] = 1
                    matrix[i*3+1][j*3+1] = 1
                    matrix[i*3+2][j*3+2] = 1
        # function to count the islands
        def dfs(r,c,matrix):
            #base
            if r < 0 or r >= M or c < 0 or c >= N or matrix[r][c]!=0:
                return
            matrix[r][c] = 1 #marking as visited
            
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            for x, y in directions:
                newr,newc = r + x, c + y
                dfs(newr,newc,matrix)
        
        #main
        M,N = len(matrix),len(matrix[0])
        result = 0
        for r in range(M):
            for c in range(N):
                if matrix[r][c] == 0:
                    dfs(r,c,matrix)
                    result += 1
        return result
            
# can also do by Union find                   
class DSUF:
    def __init__(self,N):
        self.parent = [i for i in range(N)]

    def find(self,i):
        if i == self.parent[i]:
            return i
        self.parent[i] = self.find(self.parent[i])#path compression
        return self.parent[i]
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        self.parent[pv] = pu
        
# We can think of each square as being partitioned into 4 smaller triangles.
# Depending on the value of the character in square, we will merge two
# triangles in that square. (See diagram by datou12138 in comments for better understanding of square division into triangles)

# We also need to connect each square to the squares in next row or column
# as long as they are in bounds.
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        if not grid:
            return 0
        N = len(grid)
        uf = DSUF(4 * N * N)
        for r in range(N):
            for c, val in enumerate(grid[r]):
                # This flattens out the matrix and hence easier to map to union find
                region = 4 * (r * N + c)
                # Representing the triangles as north, east, south, west
                north, east, south, west = region, region + 1, region + 2, region + 3
                # Connect triangles within the square
                if val in '\ ':
                    uf.union(north, east)
                    uf.union(west, south)
                if val in '/ ':
                    uf.union(north, west)
                    uf.union(south, east)
                
                # Connect triangles with bordering triangles inside squares present
                # in neighboring rows and columns
                if r + 1 < N:
                    bottom_square_region = region + 4 * N
                    next_north = bottom_square_region
                    uf.union(south, next_north)
                    
                if r - 1 >= 0:
                    top_square_region = region - 4 * N
                    next_south = top_square_region + 2
                    uf.union(north, next_south)
                    
                if c + 1 < N:
                    right_square_region = region + 4
                    next_west = right_square_region + 3
                    uf.union(east, next_west)
                    
                if c - 1 >= 0:
                    left_square_region = region - 4
                    next_east = left_square_region + 1
                    uf.union(west, next_east)
                    
        return sum(uf.find(triangle) == triangle for triangle in range(4 * N * N))                   
    