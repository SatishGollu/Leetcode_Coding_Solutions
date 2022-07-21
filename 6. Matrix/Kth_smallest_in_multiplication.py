# Time - O(mn log mn)
    # Space - O(mn)
def findKthNumber(self, m: int, n: int, k: int) -> int:
    #brute force multiply and add it to array 
    # and then sort the number and return the value
    table = []
    for i in range(1,m+1):
        for j in range(1,n+1):
            table.append(i*j)
    table.sort()
    return table[k-1]
# Optimaization--
# Time- O(m log mn)
# Space - O(1)
def findkthNumber2(m,n,k):
    def Count(x):
        ans = 0
        for i in range(1,m+1):
            ans += min(x/i,n)
        return ans
    left,right,mid,ans = 0,m*n,0,0
    while left < right:
        mid = (left + right) >> 1
        if Count(mid) < k:
            left = mid + 1
        else:
            right = mid - 1
            ans = mid
    return ans

