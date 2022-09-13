# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        # Time- O(n)-- Space-O(n)
        #create the hashmap to count the number of nodes
        if not head:return None
        hashmap = {}
        current = head
        while current:
            if current.val in hashmap:
                hashmap[current.val] += 1
            else:
                hashmap[current.val] = 1
            current = current.next
        # removing duplicates referencing hashmap
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while head:
            if hashmap[head.val] > 1:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next
                
            
        
            
            
            
        