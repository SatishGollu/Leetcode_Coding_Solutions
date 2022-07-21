import time


def Insertion_sort(arr):
    arr_length = len(arr)
    for i in range(1,arr_length):
        anchor = arr[i]
        j = i-1
        while j >= 0 and anchor < arr[j]:
            arr[j+1] = arr[j]
            arr[j] = anchor
            #decrement j
            j = j-1

    return arr




if __name__ == '__main__':
    start_time = time.time()
    arr = [77,97,17,57,67,7,87,47,37,27]
    print(Insertion_sort(arr))
    print('%s seconds' % (time.time() - start_time))
