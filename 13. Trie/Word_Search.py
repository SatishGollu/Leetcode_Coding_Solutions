
from collections import defaultdict, Counter
class Solution:   
    def exist(self, board, word):
        ROWS = len(board)
        COLS = len(board[0])
        path = set()                
        
        def dfs(row,col,i):
            #base-we find match in each letter in word
            if i == len(word):
                return True
            if (row < 0 or row >= ROWS or col < 0 or col >= COLS or 
                  word[i]!= board[row][col] or (row,col) in path):
                    return False
            path.add((row,col))
            #check in all 4 directions
            res = (dfs(row+1,col,i+1) or
                   dfs(row-1,col,i+1) or
                   dfs(row,col+1,i+1) or
                   dfs(row,col-1,i+1))
            
            #cleaning the path
            path.remove((row,col))
            
            return res
        # To prevent TLE,reverse the word, if frequency of the first letter is more than the last letter's
        board_count =defaultdict(int,sum(map(Counter,board),Counter()))
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):return True
        return False
                    
# Time Complexity: O(N⋅3^L) where N is the number of cells in the board and L is the length of the word to be matched.
# Space Complexity: O(L) where L is the length of the word to be matched.     

# using Hash map we can minimize the number of searches
import collections
from collections import defaultdict,Counter
def exist( board, word):
	ROW,COL = len(board),len(board[0])
	path = set()
	dic = defaultdict(set)
	for r in range(ROW):
		for c in range(COL):
			dic[board[r][c]].add((r,c))
	

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
	for r,c in dic[word[0]]:
		if dfs(r,c,0):
			return True
	return False
	
# USING TRIE
class TrieNode:
    def __init__(self):
        self.child = {}
        self.parent = None
        self.isWord = False
        self.no_words_downwards = 0
    
    def prune(self,node):
        while node:
            node.no_words_downwards -= 1
            node = node.parent
class Trie:
    def __init__(self):
        self.root = TrieNode()
    #add word
    def add_word(self,word):
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
            node.no_words_downwards += 1
        node.isWord = True

class Solution:
    def exist(self, board: List[List[str]], word) -> List[str]:
        trie = Trie()
        
        trie.add_word(word)

        ROWs,COLs = len(board),len(board[0])
        result = set()

        #backtrack function
        def dfs(r,c,node,path):
            #base
            if node.isWord:
                result.add(path)
                node.isWord = False
                node.prune(node)
            if (r < 0 or c < 0 or r >= ROWs or c >= COLs):
                return
            temp = board[r][c]
            if temp not in node.child or node.child[temp].no_words_downwards == 0:
                return
            board[r][c] = "$"
            #directions
            dfs(r + 1, c, node.child[temp],path+temp)
            dfs(r - 1, c, node.child[temp],path+temp)
            dfs(r , c + 1, node.child[temp],path+temp)
            dfs(r , c - 1, node.child[temp],path+temp) 
            # cleaning the space
            board[r][c] = temp
        #get the r,c to start searching
        for r in range(ROWs):
            for c in range(COLs):
                dfs(r,c,trie.root,"")
        return result


if __name__ == "__main__":
	board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
	words = "ABCCED"
	print(exist(board,words))