def searchMatrix(matrix, target):
        # brute force
        # Time- O(m*n)
        # Space - O(1)
        m = len(matrix[0])
        n = len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True
        return False

#optimaization 
# Binary search - Time-O(log(mn)) - Space O(1)
def searchMatrix(matrix, target):
        # optimaization-- Time- O(m+n), Space - O(1)
        m = len(matrix[0])
        n = len(matrix)
        left = 0
        right = m - 1
        # binary search for the target element
        while left >= 0 and left < n and right >= 0 and right < m:
            mid = matrix[left][right]
            if mid == target:
                return True
            elif target < mid:
                right -= 1
            elif target > mid:
                left += 1
        return False
                