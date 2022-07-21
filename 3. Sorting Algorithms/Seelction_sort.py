"""def find_min_element(arr):
    arr_length = len(arr)
    min_ele = arr[0]
    for i in range(arr_length):
        if arr[i] < min_ele:
            min_ele = arr[i]
    return min_ele"""

def Selection_sort(arr):
    arr_size = len(arr)
    for i in range(arr_size):
        min_index = i
        for j in range(min_index+1,arr_size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

#my way of coding
def Selection_sort2(arr):
    arr_size = len(arr)
    for i in range(arr_size):
        for j in range(i+1,arr_size):
            if arr[j] < arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr


if __name__ == '__main__':
    arr = [78,12,2,15,8,61,53,23,27]
    Selection_sort2(arr)
    print(arr)
