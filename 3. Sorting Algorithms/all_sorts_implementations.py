#selection sort
arr = [29,72,98,13,87,66,52,51,36]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(min_index+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

selection_sort(arr)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-1-i):
            k = j+1
            if arr[j] > arr[k]:
                arr[j],arr[k] = arr[k],arr[j]
                swapped = True
        if not swapped:
            break
    return arr
arr = [29,72,98,13,87,66,52,51,36]
bubble_sort(arr)
arr_text = ['db11','amg gt','m4','mustang']
bubble_sort(arr_text)



# insertion sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        anchor = arr[i]
        j = i-1
        while j >= 0 and arr[j] > anchor:
            #swap
            arr[j+1] = arr[j]
            arr[j] = anchor
            #decrement j
            j = j-1
    return arr
insertion_sort(arr)

arr = [29,72,98,13,87,66,52,51,36]
# Mergesort
def mergesort(arr):
    n = len(arr)
    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)

        #joining back the elements
        i = j= k= 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i +=1
            else:
                arr[k] = right[j]
                j +=1
            k += 1
        #when we run out of elements in left or right
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


mergesort(arr)

#Quicksort
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1

            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quicksort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        #Recursive call on left pivot
        quicksort(arr,low,pi-1)
        #recursive call on right
        quicksort(arr,pi+1,high)

    return arr

array = [10,14,28,11,7,16,30,50,25,18]
quicksort(array,0,len(array)-1)


#counting sort
def countingsort(arr):
    n = len(arr)
    high = max(arr)
    counting = [0] * (high+1)
    #corresponding count for every element
    for i in arr:
        counting[i] += 1

    #sum
    for i in range(1,high+1):
        counting[i] += counting[i-1]

    #calculate element position
    result = [0] * n
    i = n-1
    while i >= 0:
        curr_val = arr[i]
        counting[curr_val] -= 1
        new_position = counting[curr_val]
        result[new_position] = curr_val
        i -= 1
    return result

arr =[125,52,378,1545,385,1353]
countingsort(arr)

arr2 = [10,14,28,11,7,16,30,50,25,18]

countingsort(arr2)

#Radixsort
#1- counting sort
def counting_sort(array,place):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    #calculate count of elements
    for i in range(0,n):
        index = array[i] // place
        count[index % 10] += 1
    #cumulative count
    for i in range(1,10):
        count[i] += count[i-1]
    #place the elements in sorting order
    i = n-1
    while i >= 0:
        index = array[i]//place
        output[count[index%10]-1] = array[i]
        count[index%10] -= 1
        i -= 1

    for i in range(0,n):
        array[i] = output[i]
#main function to implement Radixsort
def radix_sort(array):
    #get maximum element
    max_element = max(array)
    #applying counting sort to sort the elements based on
    #place value
    place = 1
    while (max_element // place) > 0:
        counting_sort(array,place)
        place *= 10

data = [121, 432, 564, 23, 1, 45, 788]

radix_sort(data)
print(data)
#
#bucket sort
class bucket:
    import math
    def buck_insertion(arr):
        n = len(arr)
        for i in range(1,n):
            anchor = arr[i]
            j = i-1
            while j >= 0 and arr[j] > anchor:
                #swap
                arr[j+1] = arr[j]
                arr[j] = anchor
                j -=1

    def bucket_sort(arr):
        n = len(arr)
        maxi = max(arr)
        divider = math.ceil((maxi+1)/n)
        #creating 10 buckets
        buckets=[]
        for i in range(0,10):
            buckets.append([])
        #adding values to the buckets
        for i in range(0,n):
            j = math.floor(arr[i]/divider)
            buckets[j].append(arr[i])
        #sorting each bucket
        for i in range(1,len(buckets)):
            buck_insertion(buckets[i])
        result = []
        for s in buckets:
            result = result + s
        return result
