# Time- O(n), Space - O(1)
def search(self, nums: List[int], target: int) -> int:
        # brute force
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

# optimal one Time- O(logn), Space O(1)
def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        #checking for array which is in increasing order
        while left <= right:
            mid = (left + right) // 2
            #if middle value is target return target
            if nums[mid] == target:
                return mid

            # if mid is greater than starting element then the array is in increasing order
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid-1
                else:
                    left = mid +1
            else:
                # if mid is not greater than starting element
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1
