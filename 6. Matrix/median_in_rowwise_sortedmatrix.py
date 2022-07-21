m = [ [1, 3, 5], [2, 6, 9], [3, 6, 9]]
# naive approch -- copy every elemet into a data structure
# and sort the array and fine median value
#Time- O(M*N log M*N)
#Space - O(M*N)
def medin_mat(m):
    array = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            array.append(m[i][j])
    array.sort()
    mid = len(array)//2
    if len(array) % 2 == 0:
        return (array[mid-1] + array[mid])/2
    else:
        return array[mid]
medin_mat(m)

# optimaizaiton
#using binary search
def binaryMedium(matrix,row,col):
    import bisect
    #minimum value
    minn = matrix[0][0]
    maxx = 0

    # finding minumum and maximum value of matrix by traversing 
    # each row
    for i in range(row):
        if matrix[i][0] < minn:
            minn = matrix[i][0]
        if matrix[i][col-1] > maxx:
            maxx = matrix[i][col-1]
    #desired mid 
    desired = (row * col +1)//2
    #For a number to be median, there should be (r*c)/2 numbers
    #smaller than that number. 
    while minn < maxx:
        mid = minn + (maxx-minn) // 2
        place = 0
        #no of elements smaller then or equal to mid
        for i in range(row):
            j = bisect.bisect_right(matrix[i],mid)
            place += j
        if place < desired:
            minn = mid + 1
        else:
            maxx = mid
    return minn

if __name__ == "__main__":
    m = [ [1, 3, 5], [2, 6, 9], [3, 6, 9]]
    print(binaryMedium(m,len(m[0]),len(m)))


