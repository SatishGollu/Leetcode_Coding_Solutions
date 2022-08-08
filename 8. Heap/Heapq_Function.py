#Heapq_Function
import heapq


heap = [3,6,5,0,8,2,1,9]
heapq.heapify(heap)
heapq.heappush(heap,12)
heapq.heappush(heap,17)
heapq.heappop(heap)
heapq.heappushpop(heap,2)
heapq.heapify(heap)
heapq.nlargest(5,)