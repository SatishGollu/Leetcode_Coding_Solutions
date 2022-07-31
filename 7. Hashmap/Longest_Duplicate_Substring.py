class Solution:
    # Rabin-Karp Time- O(NlogN), Space O(N)
    def search(self, l: int, base: int, prime: int, n: int, nums: List[int]) -> str:
        #calculating the hash of the substring s[:l]
        h = 0
        for i in range(l):
            h = (h*base+nums[i])%prime
        #hash function to store already seen values
        seen = collections.defaultdict(list)
        seen[h].append(0)
        #constant value to be used - a**l%prime
        al = pow(base,l,prime)
        for start in range(1,n-l+1):
            #compute the rolling hash in O(1) time
            h = (h*base-nums[start-1] * al + nums[start+l-1]) % prime
            if h in seen:
                #check if any substring matches any of the previous substring
                curr_substring = nums[start:start+l]
                if any(curr_substring == nums[index:index+l] for index in seen[h]):
                    return start
            seen[h].append(start)
        return -1
                    
    
    
    def longestDupSubstring(self, s: str) -> str:
        #prime value to avoid overflow of hash function
        prime = 10**9 + 7
        # base value for rolling hash
        base = 26
        n = len(s)
        #converting string to intergers of array to implementt constanct time slice
        nums = [ord(s[i])- ord('a')  for i in range(n)]
        #use binary search to find longest duplicate substring
        start = -1
        left,right = 1,n
        while left < right:
            #lenght of longest substring
            l = (left + right) >> 1
            start_of_dupe = self.search(l,base,prime,n,nums)
            if start_of_dupe == -1:
                right = l
            else:
                left = l+1
                start = start_of_dupe
        #return sub string if any begins at index start and ends at start+left
        return s[start:start+left-1]
                
        