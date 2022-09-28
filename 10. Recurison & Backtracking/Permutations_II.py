class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # to get the unique take a set
        result = []
        perm = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1
        #backtrack function
        def dfs():
            #base
            if len(perm) == len(nums):
                result.append(perm.copy())
                return 
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    
                    dfs()
                    count[n] += 1
                    perm.pop()
            
        dfs()
        return result
            
            

        
        
        
        
            
        