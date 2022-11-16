class TrieNode:
    def __init__(self):
        self.child = dict()
        self.count = 0
        self.word_end = 0
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def prefixCount(self, words, pref):
        node = self.root
        
        # adding words to build trie
        for word in words:
            curr = node
            for c in word:
                if c not in curr.child:
                    curr.child[c] = TrieNode()
                curr = curr.child[c]
                curr.count += 1
            curr.word_end += 1
            
        #search and return last prefix count
        curr = self.root
        for c in pref:
            if c not in curr.child:
                return 0
            curr = curr.child[c]
        return curr.count
                
                
                    
        