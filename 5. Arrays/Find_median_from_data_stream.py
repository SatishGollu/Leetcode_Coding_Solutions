# my way -- using inbuilt sort function
# Time - O(nlogn)
# Space - O(n) to hold the input container
class MedianFinder:

    def __init__(self):
        self.array = []


    def addNum(self, num: int) -> None:
        return self.array.append(num)



    def findMedian(self) -> float:
        self.array.sort()
        n = len(self.array)
        left = 0
        right = n-1
        mid = (left + right)//2
        if n % 2:
            # odd
            return self.array[mid]
        else:
            #even
            return (self.array[mid+1] + self.array[mid])/2

# Optimal way
class MedianFinder:
    #importing heapq
    import heapq

    def __init__(self):
        #initializing the data structure
        #two heaps, large,small--min heap and max heap
        self.small,self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        #make sure every number in small is <= every number in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        #if it is uneven size
        if len(self.small) > len(self.large)+1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (self.large[0] - self.small[0])/2

# above code with same complexity but with fewer lines
# of code
class MedianFinder:
    #importing heapq
    import heapq

    def __init__(self):
        #initializing the data structure
        #two heaps, large,small--min heap and max heap
        self.small,self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large,-heapq.heappop(self.small))
        #if it is uneven size
        if len(self.small) < len(self.large):
            heapq.heappush(self.small,-heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.large) != len(self.small):
            return -self.small[0]
        else:
            return (self.large[0] - self.small[0])/2
