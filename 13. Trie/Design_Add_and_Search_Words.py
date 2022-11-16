#TIME- O(26^M) where M is the length of the word; At each node 
# due to dot we search in 26 more branches untill we 
# find the search.
class TrieNode:
    def __init__(self):
        self.child = dict()
        self.word_end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.word_end = True
            

    def search(self, word: str) -> bool:
        def dfs(position,root):
            curr = root
            for i in range(position,len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.child.values():
                        if dfs(i + 1,child):
                            return True
                    return False

                else:
                    if c not in curr.child:
                        return False
                    curr = curr.child[c]
            return curr.word_end
        return dfs(0,self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)