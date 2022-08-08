import collections
import heapq
def topKFrequent(nums, k):
    #pythonic brute force 
    # Time- O(nlogn)- becuase of using sorted function
    # Space - O(n)
    result = collections.OrderedDict()
    for each in nums:
        result[each] = result.get(each,0) + 1
    result = sorted(result.items(),key=lambda x:x[1])
    ans = [x for x,y in result]
    return ans[-k:]

#optimized version-  O(n)
# we can also do by using heap -which is O(klog n)
def topKFrequent(nums, k):
    # using bucket sort
    # Time- O(n)
    # Space - O(n)
    mapping ={} #for key value pairs
    for each in nums:
        mapping[each] = mapping.get(each,0) + 1
    # add frequencies to the list
    freq = [[] for i in range(len(nums) + 1)]
    
    for value,count in mapping.items():
        freq[count].append(value)
    #add top k frequent elements to the array
    result = []
    for i in range(len(freq)-1,0,-1):
        for values in freq[i]:
            result.append(values)
            if len(result) == k:
                return result
#using heap
#Time  - O(n log k)
#space - O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #using heap- Time-O(n log k) and space - o(n)
        #initiate hashmap for mapping key values frequency
        hashmap = {}
        for each in nums:
            if each in hashmap:
                hashmap[each] += 1
            else:
                hashmap[each] = 1
        #using heap 
        heap = []
        for key in hashmap:
            heapq.heappush(heap,(-hashmap[key],key))
        #popping k times
        right = 0
        result = []
        while right < k:
            popped_element = heapq.heappop(heap)
            result.append(popped_element[1])
            right += 1
        return result
            