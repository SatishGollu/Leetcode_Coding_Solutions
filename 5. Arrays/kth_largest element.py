nums = [3,6,4,7,8,9,77]
#naive way--nlogn complexity
def kth_largest(nums,k):
    n = len(nums)
    nums.sort()
    return nums[n-k]
#my quicksort implementation(just for practice)
# quick sort
def quicksort(arr,low, high):

    def partition(arr,low,high):
        pivot = arr[high]
        i = low -1
        for j in range(low,high):
            if arr[j] <= pivot:
                i +=1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],pivot = pivot,arr[i+1]
        return i+1
    #now let's do the sorting
    if low < high:
        pi = partition(arr,low,high)
        #for left
        quicksort(arr,low,pi-1)
        #for right
        quicksort(arr,pi+1,high)
    return arr
quicksort(nums,0,len(nums)-1)

# best method to solve with O(n) average complexity
def findklargerst(nums,k):
    #rewriting the k
    k = len(nums)-k

    #partition by doing quick select
    def quickselect(low, high):
        pivot = nums[high]
        i = low
        for j in range(low, high):
            if nums[j] <= pivot:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1

        nums[i],nums[high] = nums[high],nums[i]

        if i  > k: return quickselect(low,i-1)
        elif i < k: return quickselect(i + 1, high)
        else: return nums[i]
    return quickselect(0,len(nums)-1)

nums = [3,2,1,5,6,4]
k = 2
findklargerst(nums,k)
numss = [3,2,3,1,2,4,5,5,6]
kk = 4
findklargerst(numss,kk)















#
