class Solution:#nlogn - time complexity
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        n= len(nums)
        if n < 2:
            return 0
        j = n-2
        maxx = 0
        for i in range(n-1,-1,-1):
            result = nums[i]-nums[j]
            j -= 1
            if result > maxx:
                maxx = result
        return maxx
#pigeon hole bucket sort - O(n)
def maximumGap_pgn(nums):
    low = min(nums)
    high = max(nums)
    n = len(nums)
    size = high-low + 1
    if n <= 2 or high == low:
        return high-low
    holes = [0] * size
    for i in nums:
        assert isinstance(i,int),"Integers only"
        holes[i-low] = holes[i-low] + 1
    i = 0
    for each in range(size):
        while holes[each] > 0:
            holes[each] -= 1
            nums[i] = each + low
            i += 1
    return nums
#the above method is giving me memory exceed limit
a = [8, 3, 2, 7, 4, 6, 8]
a2 = [12,16,19,10,9]
maximumGap_pgn(a)
maximumGap_pgn(a3)
a3 = [21,9,25,3,37,43,49,29]

import math

math.ceil(8/7)

#o(n)-solution
class bucketsort:
    def maxgap(num):
        low = min(num)
        high = max(num)
        n = len(num)
        if low == high: return 0
        bucket_size = math.ceil((high-low)/(n-1))
        min_bucket = [math.inf] * n
        max_bucket = [-math.inf] * n
        #keep numbers into bucket
        for i in num:
            indx = (i - low)//bucket_size
            min_bucket[indx] = min(i,min_bucket[indx])
            max_bucket[indx] = max(i,max_bucket[indx])
        #scan buckets for maximum gap
        #max bucket is always greater or equal to bucketsize
        maxGap = bucket_size
        previous = max_bucket[0]
        for i in range(1,n):
            if min_bucket[i] == math.inf: continue#skip empty bucket
            maxGap = max(maxGap,min_bucket[i]-previous)
            previous = max_bucket[i]
        return maxGap


bucketsort.maxgap(a)
#
#
