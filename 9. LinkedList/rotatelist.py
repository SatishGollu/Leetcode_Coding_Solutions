class solution:
    def rotatelinkedlist(self,head,k):
        if not head or not head.next:
            return head
        # Get the Length 
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        current = head
        for _ in range(length - k - 1):
            current = current.next
        new_head = current.next
        current.next = None
        tail.next = head
        return new_head