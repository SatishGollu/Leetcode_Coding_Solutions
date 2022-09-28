class Solution:
    #Time Complexity: O(9^(m * n))
    #Space Complexity: O(1) modifying the given board
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #function to check conditons to fill the value
        def isValid(board,r,c,val):
            for i in range(0,9):
                if (board[r][i]==val):
                    return False
                if (board[i][c] == val):
                    return False
                if (board[3 * (r//3)+i//3][3*(c//3)+i%3] == val):
                    return False
            return True
        def fill_Sudoku_board(board):
            for r in range(len(board)):
                for c in range(len(board[0])):
                    if board[r][c]==".":
                        for val in range(1,10):
                            if isValid(board,r,c,str(val)):
                                board[r][c] = str(val)

                                # recurse the same for rest of elements
                                if fill_Sudoku_board(board):
                                    return True
                                else:
                                    board[r][c] = "."
                        return False
            return True
        fill_Sudoku_board(board)
        



