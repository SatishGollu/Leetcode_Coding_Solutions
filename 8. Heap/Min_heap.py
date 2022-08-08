#min heap
#building max heap
from collections import deque
#creating max_heapify
def min_heapify(arr,i):
    l = left(i)
    r = right(i)
    n = len(arr)
    smallest = i
    if l < n and arr[l] < arr[i]:
        smallest = l
    if r < n and arr[r] < arr[smallest]:
        smallest = r
    if smallest != i:
        arr[i],arr[smallest] = arr[smallest],arr[i]
        min_heapify(arr,smallest)

def left(k):
    return 2 * k # if we want 0th index then we can use 2k+1
def right(k):
    return 2 * k + 1 # for 0 index- can use 2k+2

#building max_heap
def build_min_heap(arr):
    n = len(arr)//2
    for i in range(n,0,-1):
        min_heapify(arr,i)

if __name__ == "__main__":
    arr = deque([0,3,6,5,0,8,2,1,9])
    build_min_heap(arr)
    print(arr)