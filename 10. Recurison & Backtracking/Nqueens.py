class Solution:
    def solveNQueens( n: int):
        cols = set()
        posdiag = set() # (r+c)
        negdiag = set() # (r-c)
        
        board = [["."]*n for i in range(n)]
        result = []
        def backtrack(row):
            #base
            if row == n:
                copy = ["".join(r) for r in board]
                result.append(copy)
                return 
            for col in range(n):
                if col in cols or (row+col) in posdiag or (row-col) in negdiag:
                    continue
                
                cols.add(col)
                posdiag.add(row+col)
                negdiag.add(row-col)
                board[row][col] = "Q"
                
                backtrack(row+1)
                
                cols.remove(col)
                posdiag.remove(row+col)
                negdiag.remove(row-col)
                board[row][col] = "."
                
        backtrack(0)
        return result
# TIME- O(N!)- Space(N*N)        

if __name__ == "__main__":
    n = 4
    print(Solution.solveNQueens(n))
    