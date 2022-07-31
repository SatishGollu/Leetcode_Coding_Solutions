# Time- O(mn)
# Space - O(mn)
def maximalRectangle(self, matrix: List[List[str]]) -> int:
    
    #function to divide matrix row wise to get maximum
    #rectangle area
    def divide_matrix(matrix):
        result = [[int(x) for x in matrix[0]]]
        for each in range(1,len(matrix)):
            add = [int(x)+int(y) if y!='0' else 0 for x,y in zip(result[-1],matrix[each])]
            result.append(add)
        return result
    #function to get the maximum rectangle area for each row 
    def largestRectangleArea(heights: List[int]) -> int:
        # using stack to store index and height
        stack = []
        max_area = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                area = height * (i-index)
                max_area = max(max_area,area)
                start = index
            stack.append((start,h))
        for index,height in stack:
            area = height * (len(heights)-index)
            max_area = max(max_area,area)
        return max_area
    # main
    rows = divide_matrix(matrix)
    maximum = 0
    for each in rows:
        result_area = largestRectangleArea(each)
        maximum = max(maximum,result_area)
    return maximum

    