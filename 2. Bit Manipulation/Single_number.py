from collections import defaultdict
class Solution:
    #using bit manipulation
    def singleNumber(self, nums) -> int:
        result = 0
        for each_num in nums:
            result = result ^ each_num
        return result

class using_hashmap:
    #using hash map
    def singleNumber(nums) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        for i in hash_table:
            if hash_table[i]==1:

                return i
nums = [2,2,1]
using_hashmap.singleNumber(nums)



#default dict
arr = ['a','a','b','c','d','f','f','d','d','c','s','a','a','s','c','d','e']
result = defaultdict(int)
for i in arr:
    result[i] +=1
result
