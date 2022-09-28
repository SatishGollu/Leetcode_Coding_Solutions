class Solution:
    def combinationSum(self, candidates, target: int):
        result = []
        
        def backtrack(i,curr,total):
            #base
            if total == target:
                result.append(curr[:])
                return
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            backtrack(i,curr,total+candidates[i])
            curr.pop()
            backtrack(i+1,curr,total)
            
        backtrack(0,[],0)
        return result
        