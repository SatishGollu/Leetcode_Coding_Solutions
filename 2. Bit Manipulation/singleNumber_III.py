#using bit manipulation
def singlenumber(nums):
    #difference between two numbers x and y whic were seen only once
    bitmask = 0
    for num in nums:
        bitmask = bitmask ^ num
    #rightmost 1-bit diff between x and y
    diff = bitmask & (-bitmask)
    x = 0
    for num in nums:
        #bitmask which will only contain x
        if num & diff:
            x ^= num
    return [x,bitmask^x]

nums = [1,2,1,3,2,5]
singlenumber(nums)

2^4
