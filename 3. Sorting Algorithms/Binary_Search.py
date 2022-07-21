#iterative method
def binary_search_iterative(arr,x):
    low = 0
    n = len(arr)
    high = n-1
    while low <= high:
        mid = low + (high-low)//2
        #if found at mid return it
        if  x == arr[mid]:
            return mid
        elif x < arr[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1

#Binary Search Recursive Method
def binary_search_recursive(arr,x,low,high):
    if low <= high:
        mid = low +(high-low)//2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            return binary_search_recursive(arr,x,low,mid-1)
        else:
            return binary_search_recursive(arr,x,mid+1,high)
    return -1


if __name__ == '__main__':
    array = [3, 4, 5, 6, 7, 8, 9]
    x = 4
    print(binary_search_iterative(array,8))
    print(binary_search_recursive(array,8,0,len(array)-1))
