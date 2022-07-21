class NumArray:

    def __init__(self, nums: List[int]):
        self.array = list(itertools.accumulate(nums,initial=0))


    def sumRange(self, left: int, right: int) -> int:
        return self.array[right + 1] - self.array[left]


# Time- O(n)
# space - O(n)
