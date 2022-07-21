nums = [-2,1,-3,4,-1,2,1,-5,4]

# Solution-1 brute force approch O(n2)
def maxsub1(nums):
    ans = float('-inf')
    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i,len(nums)):
            cur_sum += nums[j]
            ans = max(ans,cur_sum)
    return ans
maxsub1(nums)

# Soluion - 2 kadane's algo o(n)
def maxSubArray(self, nums: List[int]) -> int:
        #using kadane's algorithm
        max_ending_here = 0
        max_so_far = float('-inf')

        for each in range(len(nums)):
            max_ending_here = max(nums[each],max_ending_here + nums[each])
            max_so_far = max(max_so_far,max_ending_here)
        return max_so_far
