# my thought process
nums1,nums2 = [1,2,3,4],[5,6,7,8]
def merge(nums1,nums2):

    m,n = len(nums1),len(nums2)
    k = [0] * (m+n)
    curr = 0
    left,right = 0,0
    while left < len(nums1) and right < len(nums2):
        if nums1[left] <= nums2[right]:
            k[curr] = nums1[left]
            left += 1
        else:
            k[curr] = nums2[right]
            right += 1
        curr += 1
    while left < len(nums1):
        k[curr] = nums1[left]
        left += 1
        curr += 1
    while right < len(nums2):
        k[curr] = nums2[right]
        right += 1
        curr += 1
    return k

nmerge(nums1,nums2)



# optimal Time- O(log(m+n))
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        total = len(A) + len(B)
        half = total//2

        if len(B) < len(A):
            A,B = B,A
        left,right = 0,len(A)-1
        while True:
            i = (left+right)//2 # A
            j = half-i-2 # B

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i+1 < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if j+1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total %2:
                    #odd
                    return min(Aright,Bright)
                #even
                return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i+1


        
