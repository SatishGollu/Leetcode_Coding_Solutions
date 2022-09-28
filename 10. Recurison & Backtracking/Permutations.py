class Solution:
    #Time- O(n*n!)
    #Space - O(n!)
    def permute(self, nums):
        #base
        result = []
        if len(nums)==1:
            return [nums[:]]
        
        for each in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result
            