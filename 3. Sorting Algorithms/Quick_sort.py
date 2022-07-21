#Quick sort
def partition(array,low,high):
    #low = 0
    #high = len(array)-1
    #choosing the right most element as pivot
    pivot = array[high]
    #pointer for greater element
    i = low - 1
    #traverse through all elements and compare each elements
    for j in range(low,high):
        if array[j] <= pivot:
            #if element smaller that pivot then swap it with
            #greater element pointed by i
            i += 1
            #swap
            array[i],array[j] = array[j], array[i]
    #swap pivot element with greater element specified by i
    array[i+1],array[high] = array[high],array[i+1]
    #returning position from where partition is done
    return i+1

def quicksort(array,low,high):

    if low < high:
        #find pivot element such that left side of pivot are smaller
        #and right side of elements are larger elements
        pi = partition(array,low,high)

        #recursive call on left of pivot
        quicksort(array,low,pi-1)
        #recursive on right
        quicksort(array,pi+1,high)
    return array

array = [10,14,28,11,7,16,30,50,25,18]
print(quicksort(array,0,len(array)-1))
