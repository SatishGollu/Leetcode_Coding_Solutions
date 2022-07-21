import time

def Bubble_Sort(arr):
    arr_length = len(arr)
    for i in range(arr_length):
        for j in range(arr_length-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr      

def Bubble_Sort2(arr):
    arr_length = len(arr)
    for i in range(arr_length):
        swapped = False
        for j in range(arr_length-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr





if __name__ == '__main__':
    start_time = time.time()
    
    arr = [77,97,17,57,67,7,87,47,37,27]
    arr_text = ['db11','amg gt','m4','mustang']
    print(Bubble_Sort2(arr_text))
    print('%s seconds' % (time.time() - start_time))