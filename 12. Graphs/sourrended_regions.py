class Solution:
    #DFS here actually traverses O(n*m) in total because of temp color which prevents you from visiting the same cell twice. Therefore the overall time complexity is O(n + m + n*m) which is O(n*m)
    def dfs(self, i, j):
      if i<0 or j<0 or i>=self.M or j>=self.N or self.board[i][j] != "O":
          return
      self.board[i][j] = 'T'
      self.dfs(i+1,j)
      self.dfs(i-1,j)
      self.dfs(i,j-1)
      self.dfs(i+1,j)

    def solve(self, board):
        if not board: return 0
        self.board, self.M, self.N = board, len(board), len(board[0])

        for i in range(0, self.M):
            self.dfs(i,0)
            self.dfs(i,self.N-1)

        for j in range(0, self.N):
            self.dfs(0,j)
            self.dfs(self.M-1,j)

        for i,j in product(range(self.M), range(self.N)):
            board[i][j] = "X" if board[i][j] != "T" else "O"
