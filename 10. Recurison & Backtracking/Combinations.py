class Solution:
    #Time- (K*N^K)
    def combine(self, n: int, k: int):
        result = []
        
        def backtrack(start,comb):
            #base
            if len(comb) == k:
                result.append(comb[:])
            
            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1,comb)
                comb.pop()
        backtrack(1,[])
        return result
        