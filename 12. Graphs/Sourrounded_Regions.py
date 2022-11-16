class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return 0
        M = len(board)
        N = len(board[0])
        #dfs function
        def dfs(r,c):
            #base
            if r < 0 or c < 0 or r >= M or c >= N or board[r][c] != "O":
                return
            board[r][c] = "#"
            directions = [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            for x,y in directions:
                dfs(x,y)
        # finding unsurrounded regions-- edges
        #columns
        for i in range(0,M):
            dfs(i,0)
            dfs(i,N-1)
        #rows
        for j in range(0,N):
            dfs(0,j)
            dfs(M-1,j)
        #main
        for r in range(M):
            for c in range(N):
                board[r][c] = "X" if board[r][c] != "#" else "O"
        

        