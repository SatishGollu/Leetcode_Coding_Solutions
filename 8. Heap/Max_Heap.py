#building max heap
from collections import deque
#creating max_heapify
def max_heapify(arr,i):
    l = left(i)
    r = right(i)
    n = len(arr)
    largest = i
    if l < n and arr[l] > arr[i]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heapify(arr,largest)

def left(k):
    return 2 * k # if we want 0th index then we can use 2k+1
def right(k):
    return 2 * k + 1 # for 0 index- can use 2k+2

#building max_heap
def build_max_heap(arr):
    n = len(arr)//2
    for i in range(n,0,-1):
        max_heapify(arr,i)

if __name__ == "__main__":
    arr = deque([0,3,6,5,0,8,2,1,9])
    build_max_heap(arr)
    print(arr)