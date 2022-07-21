from xml.dom.minidom import Element


def linear_search(arr,n,x):
    for i in range(0,n):
        if arr[i] == x:
            return i
    return -1

if __name__ == '__main__':
    arr = [2,3,4,5,6,7,8,9]
    x = 9
    n = len(arr)
    #funciton call
    result = linear_search(arr,n,x)
    if result == -1:
        print('Element is not present in the array')
    else: 
        print('Element is present at the index',result)