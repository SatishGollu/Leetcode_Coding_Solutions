#Merge_K_sorted_lists -- musing divide and conquer
#Time = O(nlOgK)
#Space = O(n)
def merge_K_lists(lists):
    #base case
    if not lists or len(lists) == 0:
        return None
    while len(lists) > 1:
        combined_list = []
        for i in range(0,len(lists),2):
            l1 = lists[i]
            l2 = lists[i+1] if (i+1) < len(lists) else None
            combined_list.append(mergeList(l1,l2))
        lists = combined_list
        return lists[0]

#function to merge 2 lists
# TIme- O(n+m)
#Space complexity O(n)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeList(l1,l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    else:
        tail.next = l2
    return dummy.next


# using heap
from heapq import heapify,heappop,heappush
def mergeklists(lists):
    dummy = ListNode()
    tail = dummy
    heap = []
    for index,element in enumerate(lists):
        if element: 
            heappush(heap,(element.val,index))
    while heap:
        value,index = heappop(heap)
        tail.next = ListNode(value)
        tail = tail.next
        if lists[index].next:
            lists[index] = lists[index].next
            heappush(heap,(lists[index].val,index))
    return dummy.next