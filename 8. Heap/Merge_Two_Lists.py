#Merge_Two_Lists
# TIme- O(n+m)
#Space complexity O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(l1,l2):
    prehead = ListNode(-1)
    prev = prehead
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    #at least one of l1 and l2 can still have nodes 
    #at this point so connect the list to the end of the 
    #merged list
    if l1:
        prev.next = l1
    else:
        prev.next = l2
    return prehead.next