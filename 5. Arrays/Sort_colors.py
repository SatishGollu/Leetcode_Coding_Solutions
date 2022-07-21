def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
# we swap elements by using three pointers
        low = 0
        middle = 0
        high = len(nums)-1
        while middle <= high:
            if nums[middle] == 0:
                nums[low],nums[middle] =  nums[middle],nums[low]
                low += 1
                middle += 1
            elif nums[middle] == 1:
                middle +=1
            elif nums[middle] == 2:
                nums[middle],nums[high] =  nums[high],nums[middle]
                high -= 1

#using quicksort
def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #using quick sort function
        def partition (nums,low,high):
            pivot = nums[high]
            i = low
            for j in range (low,high):
                if nums[j] <= pivot:
                    nums[i],nums[j] = nums[j],nums[i]
                    i += 1
            nums[i],nums[high] = nums[high],nums[i]
            return i
        def quicksort(nums,low,high):
            if low < high:
                pi = partition(nums,low,high)
                quicksort(nums,low,pi-1)
                quicksort(nums,pi+1,high)

        quicksort(nums,0,len(nums)-1)
#using merge sort
def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #using merge sort

        n = len(nums)
        if n > 1:
            mid = n // 2
            le = nums[:mid]
            ri = nums[mid:]
            self.sortColors(le)
            self.sortColors(ri)
        #adding back elements
            i,j,k = 0,0,0
            while i < len(le) and j < len(ri):
                if le[i] < ri[j]:
                    nums[k] = le[i]
                    k += 1
                    i +=1
                else:
                    nums[k] = ri[j]
                    k += 1
                    j += 1
            #filling remaining elements after the loop
            while i < len(le):
                nums[k] = le[i]
                i += 1
                k += 1
            while j < len(ri):
                nums[k] = ri[j]
                j += 1
                k += 1
        #mergesort(nums)

        
