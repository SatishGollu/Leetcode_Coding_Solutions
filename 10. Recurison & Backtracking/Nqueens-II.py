class Solution:
    #TIME-O(N!)-- Space - O(N)
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posdiag = set()
        negdiag = set()
        def backtrack(row):
            #base
            if row == n:
                return 1
            result = 0
            for c in range(n):
                if c in cols or (row + c) in posdiag or (row-c) in negdiag:
                    continue
                cols.add(c)
                posdiag.add(row + c)
                negdiag.add(row - c)
                
                result += backtrack(row + 1)
                
                cols.remove(c)
                posdiag.remove(row + c)
                negdiag.remove(row - c)
            return result
        return backtrack(0)
        