
''' functional way'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        #Time - O(nlogn) space-O(logn)
        if not head or not head.next:
            return head
        mid = self.getmid(head)
        #now perform the divide on both halfs recursively
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergelist(left,right)
    
    #function to get mid
    def getmid(self,head):
        #divide the list in to half
        slow,fast = head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    #merge sort to sort and merge the list
    def mergelist(self,list1,list2):
        prehead = ListNode(-1)
        prev = prehead
        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
                
            prev = prev.next
        # if there are any values left in any list
        if list1:
            prev.next = list1
        else:
            prev.next = list2
        return prehead.next

# single way not having function to mid
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Time - O(nlogn) space-O(logn)
        if not head or not head.next:
            return head
        slow,fast = head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        #now perform the divide on both halfs recursively
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergelist(left,right)

    #merge sort to sort and merge the list
    def mergelist(self,list1,list2):
        prehead = ListNode(-1)
        prev = prehead
        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
                
            prev = prev.next
        # if there are any values left in any list
        if list1:
            prev.next = list1
        else:
            prev.next = list2
        return prehead.next
               