# Time- O(M*N)
# Space - O(1) since it's inplace
def rotate(matrix):

    """
    Do not return anything, modify matrix in-place instead.
    """
    left,right = 0, len(matrix)-1
    
    while left < right:
        for i in range(right-left):
            top,bottom = left,right
            
            #save the top left
            topleft = matrix[top][left + i]
            
            # move the bottom left to top left
            matrix[top][left + i] = matrix[bottom - i][left]
            
            # move the bottom right to the bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            
            #move the top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            
            #move the top left to the top right
            matrix[top + i][right] = topleft
        right -= 1
        left += 1
            