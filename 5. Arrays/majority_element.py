#using sort function
# Time - O(nlogn)
# Space - O(1)
def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


#using hashmap
# Time - O(n)
# Space - O(n)
def majorityElement(self, nums: List[int]) -> int:
        count = {}
        majority, maxcount = 0,0
        for num in nums:
            count[num] = count.get(num,0)+1
            majority = num if count[num] > maxcount else majority
            maxcount = max(count[num],maxcount)
        return majority
#using moore's voting algo
# Time - O(n)
# Space - O(1)
def majorityElement(self, nums: List[int]) -> int:
        #moore's voting algo
        count = 1
        majority = nums[0]
        for num in nums:
            if num == majority:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majority = num
                    count += 1
        return majority
