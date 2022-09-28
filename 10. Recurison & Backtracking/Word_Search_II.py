from collections import defaultdict, Counter
class Solution:
    def findWords(self, board, words):
        ROW,COL = len(board),len(board[0])
        path = set()
        dic = defaultdict(set)
        for r in range(ROW):
            for c in range(COL):
                dic[board[r][c]].add((r,c))
        result = set()

        #backtrack function
        def dfs(r,c,i):
            #base
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROW or c >= COL or
                word[i] != board[r][c] or (r,c) in path ):
                return False
            temp = board[r][c]
            board[r][c] = "$"
            #path.add((r,c))
            #directions
            res = (dfs(r + 1, c, i +1) or
                    dfs(r - 1, c, i +1) or
                    dfs(r , c + 1, i +1) or
                    dfs(r , c - 1, i +1) )
            # cleaning the space
            #path.remove((r,c))
            board[r][c] = temp
            return res
        #get the r,c to start searching
        for word in words:
            for r,c in dic[word[0]]:
                if dfs(r,c,0):
                    result.add(word)
        return result