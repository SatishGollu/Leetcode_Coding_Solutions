def subarraySum(self, nums: List[int], k: int) -> int:
    #using hashmap  & prefix sum -- TIme-O(N) , space O(N)
    hashmap = {}
    summ = 0
    count = 0
    left = 0
    while left < len(nums):
        summ += nums[left]
        if summ == k:
            count += 1
        if summ-k in hashmap:
            count += hashmap[summ-k]
        hashmap[summ] = hashmap.get(summ,0) + 1
        left += 1
    return count