class Solution:
    def detectCycle(self, head):
        # floyd tortoise and hare algo
        # time - O(n), space - O(1)
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else: return None # if not (fast and fast.next): return None
        head_pointer = head
        while slow != head_pointer:
            slow = slow.next
            head_pointer = head_pointer.next
        return slow