#using hash
# Time - O(n)
# Space - O(1)
def majorityElement(self, nums: List[int]) -> List[int]:
        #using hash
        n = len(nums)
        x = n//3
        count = {}
        result = []
        for num in nums:
            count[num] = count.get(num,0) + 1
        #traversing the map
        for each in count:
            if count[each] > x:
                result.append(each)
        return result

# Time - O(n)
# Space - O(1)
def majorityElement(self, nums: List[int]) -> List[int]:
        #using moore's voting algo
        n = len(nums)
        count1,count2,majority1,majority2 = 0,0,0,1
        for num in nums:
            if num == majority1:
                count1 += 1
            elif num == majority2:
                count2 += 1
            elif count1 == 0:
                majority1 = num
                count1 = 1
            elif count2 == 0:
                majority2 = num
                count2 = 1
            else:
                count1,count2 = count1-1,count2-1
        return [each for each in (majority1,majority2) if nums.count(each) > (n//3)]
