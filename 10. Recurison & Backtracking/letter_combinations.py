#letter_combinations
class Solution:
    def letterCombinations(self, digits: str):
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno","7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = []
        if len(digits) == 0:
            return result
        def backtrack(i, path):
            #base
            if len(path) == len(digits):
                result.append(path)
                return 
            for each in dic[digits[i]]:
                backtrack(i+1,path+each)
        backtrack(0,"")
        return result
#Time- 4^n
#space - O(N)
        
            
        
        