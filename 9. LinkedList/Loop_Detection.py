class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #using hashmap 
        #Time - O(n), Space - O(n)
        hashmap = set()
        while head:
            if head in hashmap:
                return True
            hashmap.add(head)
            head = head.next
        return False

class Solution:
    def hasCycle(self, head) -> bool:
        #using floyd tortoise method 
        #Time - O(n), Space - O(1)
        slow_pointer,fast_pointer = head,head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
            
        return False