#optimal-two pointers
# Time- O(n)
# Space - O(1)

def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #nums size
        n = len(nums)
        #using two pointers for the loop
        left = 0
        right = 0
        summ = 0
        minimum_size = float('inf')
        while right < n:
            summ += nums[right]
            # if sum is greater than or equal to target
            if summ >= target:
                while summ >= target:
                    summ -= nums[left]
                    left += 1
                #returning the window size and storing in window variable
                window = (right-left) + 2
                #storing minimum size of variable that equals to the target
                minimum_size = min(minimum_size, window)
            right += 1
        return 0 if minimum_size == float('inf') else minimum_size


# a brute force solution woulb be O(n2) with two loops
