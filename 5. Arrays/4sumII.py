def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        #Time- O(n2)
        # Space- O(n2) - worst case the dict will have n2 different unique pairs
        cnt = 0
        hashmap = defaultdict(int)
        # loop for first 2 lists
        for i in nums1:
            for j in nums2:
                hashmap[i+j] += 1
        for k in nums3:
            for l in nums4:
                cnt += hashmap[-(k+l)]
        return cnt
