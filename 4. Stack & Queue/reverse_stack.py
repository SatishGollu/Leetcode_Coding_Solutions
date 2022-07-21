#reversing a stack without using extraspace

class stacknode:
    def __inti__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None
    #push and pop operations
    def push(self,data):
        if self.top == None:
            self.top = stacknode(data)
            return
        s = stacknode(data)
        s.next = self.top
        self.top = s

    def pop(self):
        s = self.top
        self.top = self.top.next
        return s
    #print contents of stack
    def display(self):
        s = self.top

        while s!= None:
            print(s.data, end = ' ')
            s = s.next

    #reverse stack using simple LinkedList
    #reversal logic

    def reverse(self):
        prev = self.top
        cur = self.top
        cur = cur.next
        succ = None
        prev.next = None

        while cur ! = None:
            succ = cur.next
            cur.next = prev
            prev = cur
            cur = succ
        self.top = prev
if __name__=='__main__':

    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print("Original Stack")
    s.display()
    print()

    # Reverse
    s.reverse()

    print("Reversed Stack")
    s.display()




















from collections import deque
#function to insert an item at the bottom of
#given stack
def insert_at_bottom(s,item):
    #if stack is empty insert the given item
    #at the bottom of stack
    if not s:
        s.append(item)
        return
    top = s.pop()
    insert_at_bottom(s,item)
    s.append(top)


#recursive function to reverse a given stack
def reverse_stack(s):
    if not s:
        return

    item = s.pop()
    reverse_stack(s)
    insert_at_bottom(s,item)

if __name__ == '__main__':

    s = deque(range(1, 6))
    print('Original stack is', s)
    reverseStack(s)
    print('Reversed stack is', s)
