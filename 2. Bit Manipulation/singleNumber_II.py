from collections import defaultdict
from collections import Counter
nums = [4,2,3,2,4,4,2]

#using hashmap
def hashmap(nums):
    result = defaultdict(int)
    for i in nums:
        result[i] += 1
    for i in result:
        if result[i] == 1:
            return i
hashmap(nums)

#using Counter
def hash_counter(nums):
    result = Counter(nums)
    for i in result.keys():
        if result[i] == 1:
            return i
hash_counter(nums)

class Solution:
    #using bitwise operators
    def singleNumber(self, nums: List[int]) -> int:
        ones = twice = 0
        for each_num in nums:
            ones = ~twice & (ones ^ each_num)
            twice = ~ones & (twice ^ each_num)
        return ones
