#reverse a linked list using python
# 1. iterative approach- Time-O(n),Space - O(1)
class Solution:
    def reverseList(self, head):
        # iterative approach
        prev_node = None
        curr_node = head
        next_node = None
        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        head = prev_node
        return head
# 2. recursive approach
class Solution:
    def reverseList(self, head):
        return self.reverse(head)
        #recursive approach
        #Time - O(n),- Space - O(n)- because of implicit stack
    def reverse(self,node,prev = None):
        #base condition
        if node is None:
            return prev
        n = node.next
        node.next = prev
        return self.reverse(n,node)
