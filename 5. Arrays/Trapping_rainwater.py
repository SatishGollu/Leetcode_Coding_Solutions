
def trap(self, height: List[int]) -> int:
    #1st optimal solution - Time-O(n), Space - O(n)
    #base condition
    if len(height) <= 2:
        return 0
    #length
    n = len(height)
    #store left max from each bar
    left,right = [None] * n,[None] * n
    left[0] = 0
    l_max = height[0]
    for i in range(1,n):
        left[i] = l_max
        l_max = max(l_max,height[i])
    #store right max from each bar
    right[n-1] = 0
    r_max = height[n-1]
    for j in range(n-2,-1,-1):
        right[j] = r_max
        r_max = max(r_max,height[j])
    #parsing array to trap the water
    trapped_water = 0
    for i in range(1,n-1):
        if height[i] < left[i] and height[i] < right[i]:
            trapped_water += (min(left[i],right[i]) - height[i])
    return trapped_water
