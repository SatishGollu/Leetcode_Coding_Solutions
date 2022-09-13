# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedlist(self,head,k):
        prev_node = None
        current_node = head
        next_node = None
        while k:
            next_node = current_node.next
            current_node.next = prev_node #new head
            prev_node = current_node
            current_node = next_node
            k -= 1
        return prev_node
            
    def reverseKGroup(self, head, k: int):
        count = 0
        current_node = head
        #check if there are at least k nodes
        while count < k and current_node:
            current_node = current_node.next
            count += 1
        #if we have k nodes
        if count == k:
            #reverse the first k nodes
            reversedHead = self.reverseLinkedlist(head,k)
            head.next = self.reverseKGroup(current_node,k)
            return reversedHead
        return head
# ITERATIVE PROCESS
# TIME- O(N), SPACE - O(1)
def reverse(self,head, k):
        # Code here
        dummy = ListNode(0)
        dummy.next = head
        prev_node,current_node,next_node = dummy,dummy,dummy
        count = 0
        while current_node.next:
            count += 1
            current_node = current_node.next
        while count >= k:
            current_node = prev_node.next
            new_node = prev_node.next
            next_node = current_node.next
            for _ in range(k-1):
                tail_node = next_node.next
                next_node.next = current_node
                current_node = next_node
                next_node = tail_node
            prev_node.next = current_node
            new_node.next = next_node
            prev_node = new_node
            count -= k
        return dummy.next
