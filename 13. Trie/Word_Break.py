# Dp + memoization
from collections import deque


class Solution:
    #Time- O(n.n.n), Space-O(N)
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i] is True:
                    break
        return dp[0]
#recursive solution- TLE
class Recursive_Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        #recursive solution- Time O(2^n)
        
        def recurse(s,wordDict,start):
            #base
            if start == len(s):
                return True
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict and recurse(s,wordDict,end):
                    return True
            return False
        return recurse(s,wordDict,0)   
# recursive with momoization
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        #recursive with memoization
        memo = {}
        def recurse(s,wordDict,start):
            #base
            if start == len(s):
                return True
            if start in memo:
                return memo[start]
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict and recurse(s,wordDict,end):
                    memo[start] = True
                    return True
            memo[start] = False
            return False
        return recurse(s,wordDict,0)
## Time complexity : O(n^3)). Size of recursion tree can go up 
# to n^2.
#Space complexity : O(n). The depth of recursion tree 
# can go up to n.

# using BFS-- same time complexity and space
class BFS_Solution:
    from collections import deque
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        q = deque()
        visited = set()
        q.append(0)

        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start+1,len(s)+1):
                sub = s[start:end]
                if sub in word_set:
                    q.append(end) #end is the new beginning
                    if end == len(s):
                        return True
            visited.add(start)
        return False


# USING TRIE -- OPTIMAIZATION - O(N^2 + T)
# SPACE - O(N+T)
class TrieNode:
    def __init__(self):
        self.child = dict()
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    # building a tire
    def addword(self,word):
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
        node.isWord = True
class Solution:
    def wordBreak(self, s, wordDict) -> bool:
        # create a trie of wordDict
        trie = Trie()
        for word in wordDict:
            trie.addword(word)
        #length of s
        n = len(s)
        # take a dp to keep track
        dp = [False] * (n+1)
        dp[n] = True
        
        for i in range(n-1,-1,-1):
            curr = trie.root
            for j in range(i+1,n+1):
                c = s[j-1]
                if c not in curr.child:
                    break
                curr = curr.child[c]
                if curr.isWord and dp[j]:
                    dp[i] = True
                    break
        return dp[0]
        
        
        
        
        
        
        
        
        
        