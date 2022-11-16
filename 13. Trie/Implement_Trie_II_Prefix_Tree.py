class TrieNode:
    def __init__(self):
        self.child = {}
        self.word_end = 0
        self.word_starts = 0
class Trie:

    def __init__(self):
        self.root = TrieNode()  

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
            curr.word_starts += 1
        curr.word_end += 1
        

    def countWordsEqualTo(self, word: str) -> int:
        curr=self.root
        for c in word:
            if c not in curr.child:
                return 0
            curr = curr.child[c]
        return curr.word_end
        

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr.child:
                return 0
            curr = curr.child[c]
        return curr.word_starts
        

    def erase(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                return 0
            curr = curr.child[c]
            curr.word_starts -= 1
        curr.word_end -= 1
        return curr.word_end
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)