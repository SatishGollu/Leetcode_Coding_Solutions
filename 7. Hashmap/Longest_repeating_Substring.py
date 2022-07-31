# Approach 1 
#  binary search + hashset of already seen things
    # Time- O(N log N) - average case and O(N2) in the worst case
    # Space complexity - O(N2) to keep the hashset
    
def search(self,l,n,s):
    seen = set()
    for start in range(0,n - l + 1):
        tmp = s[start:start + l]
        if tmp in seen:
            return start
        seen.add(tmp)
    return -1

def longestRepeatingSubstring(self, s: str) -> int:
    n = len(s)
    #binary search l = repeating string length
    left, right = 1,n
    while left < right:
        l = (left + right) >> 1
        if self.search(l,n,s) == -1:
            right = l
        else:
            left = l + 1
    return left-1
# Approach 2
#To reduce the memory consumption by the hashset structure, 
# one could store not the full strings, but their hashes.
#The drawback of this approach is a time performance, 
# which is still not always linear.
#       Time - O(N log N) average case and O(N2) in worst case
#       Space - O(N) to keep the hashset
def search(self,l,n,s):
    seen = set()
    for start in range(0,n - l + 1):
        tmp = s[start:start + l]
        h = hash(tmp)
        if h in seen:
            return start
        seen.add(tmp)
    return -1

def longestRepeatingSubstring(self, s: str) -> int:
    n = len(s)
    #binary search l = repeating string length
    left, right = 1,n
    while left < right:
        l = (left + right) >> 1
        if self.search(l,n,s) == -1:
            right = l
        else:
            left = l + 1
    return left-1
# i've run the test and it's signigicantly faster than approach 1
#approach 3
#Rabin-karp with polynomial rolling hash
    # Time - O(NlogN) --O(logN) for binary search and O(N) for rabin karp
     # Space - O(N)
def search(self, l: int, a: int, modulus: int, n: int, nums):
    #compute the hash of string s[:l]
    h = 0
    for i in range(l):
        h = (h * 26 + nums[i])%modulus
    #already seen hashes of strings of length l
    seen = {h}
    #constant value to be used oftern : a ** l # modulus
    al = pow(a,l,modulus)
    for start in range(1,n-l+1):
        h = (h*a-nums[start -1] * al+nums[start+l-1])%modulus
        if h in seen:
            return start
        seen.add(h)
    return -1


def longestRepeatingSubstring(self, S):
    n = len(S)
    #convert string to array of intergers to implement constant time slice
    nums = [ord(S[i]) - ord('a') for i in range(n)]
    #base value for rolling hash
    a = 26
    #modulus value for the rolling hash function to avoid overflow
    modulus = 2**24
    
    #binary search l = repeating string length
    left,right = 1,n
    while left < right:
        l = (left+right) >> 1
        if self.search(l,a,modulus,n,nums) == -1:
            right = l
        else:
            left = l+1
    return left -1
    