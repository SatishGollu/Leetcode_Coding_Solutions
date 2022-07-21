#implementing queue using stack
# enqueu costly
class MyQueue:

    def __init__(self):
    """
    initializing stack
    """
    self.stack1 = []
    self.stack2 = []

    def push(self, x: int) -> None:
        #pushing the element
        while len(self.stack1):
            top = self.stack1.pop()
            self.stack2.append(top)
        self.stack1.append(x)
        while len(self.stack2):
            top = self.stack2.pop()
            self.stack1.append(top)

    def pop(self) -> int:
        return self.stack1.pop()


    def peek(self) -> int:
        #getting the front element
        return self.stack1[-1]


    def empty(self) -> bool:
        return len(self.stack1)==0
