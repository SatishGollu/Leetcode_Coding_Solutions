def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #using two pointers -- Time- O(n3)
        #sorting the nums
        nums.sort()
        result = []
        #length of nums
        n = len(nums)

        for i in range(0,n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left,right = j+1,n-1
                while left < right:
                    summ = nums[i] + nums[j] + nums[left] + nums[right]
                    if summ > target:
                        right -= 1
                    elif summ < target:
                        left += 1
                    else:
                        result.append([nums[i] , nums[j] , nums[left] , nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
        return result
#O(n3) is the optimized solution for this problem
