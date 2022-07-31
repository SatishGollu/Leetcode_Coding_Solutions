import collections
def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time- O(n2)- where n = 9
        #Space - O(n)
        #using hashset
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set) 
        #key is to divide by 3 to get the 3*3 r//3,c//3
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3,c//3)]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return True
        