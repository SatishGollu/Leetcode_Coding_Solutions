class TrieNode:
    def __init__(self):
        self.child = dict()
        self.val = 0
class Trie:
    def __init__(self,n):
        self.root = TrieNode() 
        self.n = n
    # construct trie for given number
    def add_num(self,num):
        curr = self.root
        for shift in range(self.n,-1,-1):
            val = 1 if num & (1 << shift) else 0
            if val not in curr.child:
                curr.child[val] = TrieNode()
            curr = curr.child[val]
        curr.val = num
    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_len = len(bin(max(nums)))-2
        construct_trie = Trie(max_len)
        for num in nums:
            construct_trie.add_num(num)
        
        result = 0
        for num in nums:
            node = construct_trie.root
            for shift in range(max_len,-1,-1):
                val = 1 if num & (1 << shift) else 0
                node = node.child[1-val] if (1-val) in node.child else node.child[val]
            result = max(result,num ^ node.val)
        return result
        
# Time - O(N).It takes O(L) to insert a number in Trie, and O(L) 
# to find the max XOR of the given number with all already inserted ones       
#SPACE-O(1).since one needs at maximum O(2^L)=O(M) space to keep Trie, 
# and L and M could be considered as constants here because of 
# input limitations.        
        
        
        
        
        