# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        # adding values to the list
        list1 = []
        curr = head
        while curr:
            list1.append(curr.val)
            curr = curr.next
        reverse_list = list1[::-1]
        return list1 == reverse_list

class Solution:
    def isPalindrome(self, head):
        #Time - O(N), Space - O(1)
        #using two pointer approach
        slow = head
        fast = head
        
        # finding mid (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #reverse second half
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        #check palindrome
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


        