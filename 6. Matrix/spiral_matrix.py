# Time- O(m*n)
# Space - O(m*n)
def spiralOrder(matrix):
    result = []
    if len(matrix)==0 or len(matrix[0])==0:
                                return result
    left,right = 0,len(matrix[0])
    top,bottom = 0,len(matrix)

    while left < right and top < bottom:
        #go left to right and get every value in the top row
        for i in range(left,right):
            result.append(matrix[top][i])
        top +=1
        #get every i in the right most column
        for i in range(top,bottom):
            result.append(matrix[i][right-1])
        right -=1
        if not (left < right and top < bottom):
            break
        #get every i in the bottom column
        for i in range (right-1, left-1,-1):
            result.append(matrix[bottom-1][i])
        bottom -=1
        #get every i in the left column
        for i in range(bottom-1,top-1,-1):
            result.append(matrix[i][left])
        left +=1
    return result
# second type
def spiralOrder2(matrix):
    n, m = len(matrix[0]), len(matrix)
    x, y, dx, dy = 0, 0, 1, 0
    ans = []
    for _ in range(m*n):
        if not 0 <= x+dx < n or not 0 <= y+dy < m or matrix[y+dy][x+dx] == "*":
            dx, dy = -dy, dx
            
        ans.append(matrix[y][x])
        matrix[y][x] = "*"
        x, y = x + dx, y + dy
    
    return ans        

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(spiralOrder2(matrix))
