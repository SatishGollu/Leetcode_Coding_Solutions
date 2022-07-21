def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    import bisect
    #using binary search 
    #Time complexity is O(n * log(A)), where A is difference between maximum and minimum values in our matrix.
    #getting the minimum and maximum values from matrix
    # as matrix is sorted we can say that first indexed is minumum and 
    # last indexed is maximum
    m = len(matrix)
    #base condition
    if m <= 1:
        return matrix[0][0]
    left = matrix[0][0]
    right = matrix[m-1][m-1]
    result = 0
    #function to get the count 
    def countt(mid):
        ans = 0
        for i in range(m):
            res = bisect.bisect_right(matrix[i],mid)
            ans += res
        return ans
    while left <= right:
        mid = (left + right) >> 1
        if countt(mid) < k:
            left = mid + 1
        else:
            right = mid -1
            result = mid
    return result
            