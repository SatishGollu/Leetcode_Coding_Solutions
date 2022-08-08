#brute force
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #base
        if k > len(nums):
            return
        result = []
        for i in range(0,len(nums)-k+1):
            maxx = max(nums[i:k+i])
            result.append(maxx)
        return result
# optimaization using deque O(n)
class Solution:
    from collections import deque
    def maxSlidingWindow(nums, k):
        #base
        if k==1:
            return nums
        if k > len(nums):
            return []
        #initialize deque and output
        deq = deque()
        left,right =0,0
        output = []
        while right < len(nums):
            while deq and nums[deq[-1]] < nums[right]:
                deq.pop()
            deq.append(right)
            
            if left > deq[0]:
                deq.popleft()
            if (right + 1) >= k:
                output.append(nums[deq[0]])
                left += 1
            right += 1
        return output
                               
                               
        
