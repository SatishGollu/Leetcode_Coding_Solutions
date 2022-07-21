
# brute foce method --O(n2), space- O(n)
def brute_cnt_inversion(nums):
    length = len(nums)
    inv_count = 0
    for i in range(length):
        for j in range(i+1,length):
            if nums[i] > nums[j]:
                inv_count += 1
    return inv_count
arr = [1, 20, 6, 4, 5]
brute_cnt_inversion(arr)

# optimized method --using mergesort-time- O(nlogn)
# Function to use inversion count
def Mergesort(arr,n):
    temp_arr = [0]*n
    return _mergesort(arr,temp_arr,0,n-1)
# Function which will used mergesort to count inversions
def _mergesort(arr,temp_arr,left,right):
    inv_count = 0
    if left < right:
        mid = (left + right)// 2
        #inversion counts in the left sub array
        inv_count += _mergesort(arr,temp_arr,left,mid)
        #inversion counts in the right sub array
        inv_count += _mergesort(arr,temp_arr,mid+1,right)
        #to merge two subarrays in a sorted array
        inv_count += merge(arr,temp_arr,left,mid,right)
    return inv_count

# Function to merge two subarrays in single sorted array
def merge(arr,temp_arr,left,mid,right):
    i = left
    j = mid+1
    k = left
    inv_count = 0
    #to check i and j didn't exceed their subarray limits
    while i <= mid and j <= right:
        #no inversion if arr[i] <= arr[j]
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            #inversion will occur
            temp_arr[k] = arr[j]
            inv_count += (mid-i +1)
            k += 1
            j += 1
    #copy the remaining elements fo left subarray
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
    #copying the remaining elements of right subarray
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
    # copy the sorted subarray into original array
    for each in range(left, right+1):
        arr[each] = temp_arr[each]
    return inv_count

arr = [1,20,6,4,5]
Mergesort(arr,len(arr))
