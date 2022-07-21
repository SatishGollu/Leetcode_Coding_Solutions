def minAbsDifference(nums, goal) -> int:
    import bisect
    #meet in the middle algorithm
    # function to generate all possible sums of subsets
    def subsets(nums):
        #result variable
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(sum(subset))
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            #decision not to include nums[i]
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
    # generate all possible sums for two halves of nums
    mid = len(nums)//2
    #1st part sums
    p1_sums = subsets(nums[:mid])
    # 2nd part sum
    p2_sums = subsets(nums[mid:])
    p2_sums.sort()
    ans = float("inf")
    #for each sum of 1t half, find the sum in the 2nd that give closest value to the goal
    for s in p1_sums:
        remain = goal-s
        #binary search for the value in s2 that's closest to the remaining value
        i2 = bisect.bisect_left(p2_sums,remain)
        if i2 < len(p2_sums):
            ans = min(ans,abs(remain-p2_sums[i2]))
        if i2 > 0:
            ans = min(ans,abs(remain-p2_sums[i2-1]))
        if ans == 0:
            return 0
    return ans
if __name__ == "__main__":
    nums = [5,-7,3,5]
    goal = 6
    print(minAbsDifference(nums,goal))