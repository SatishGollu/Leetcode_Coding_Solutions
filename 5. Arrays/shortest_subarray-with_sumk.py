def shortestSubarray(self, nums: List[int], k: int) -> int:
        # using deque
        presum = list(itertools.accumulate(nums,initial=0))

        deque = collections.deque([])
        res = float('inf')

        for i in range(len(nums) + 1):
            while deque and presum[i]-presum[deque[0]] >= k:
                res = min(res,i-deque[0])
                deque.popleft()
            while deque and presum[i] <= presum[deque[-1]]:
                deque.pop()

            deque.append(i)
        return -1 if res == float('inf') else res

# Time- O(n)
# Space - O(n)
