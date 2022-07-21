# Optimal -TIme O(n2)
def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorting the array
        nums.sort()
        #result variable to store
        result = []

        for i,n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            left,right = i+1,len(nums)-1
            while left < right:
                total = n + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.append([n,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result
# brute force O(n3)
