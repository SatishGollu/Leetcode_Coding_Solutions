class ListNode:
    def __init__(self,x):
        self.data = x
        self.next = None
def getJosephusPosition(m,n):
    #create a circular linked list of size n
    head = ListNode(1)
    prev = head
    for i in range(2,n+1):
        prev.next = ListNode(i)
        prev = prev.next
    prev.next = head # connecting last node to first
    
    #while only one node is left in the linked list
    pointer1 = head
    pointer2 = head
    while pointer1.next != pointer1:
        #find the mth node
        count = 1
        while count != m:
            pointer2 = pointer1
            pointer1 = pointer1.next
            count += 1
        #remove the mth node
        pointer2.next = pointer1.next
        pointer1 = pointer2.next
    return pointer1.data

if __name__ == "__main__":
    n = 4
    m = 2
    print(getJosephusPosition(m,n))