#referece link - https://leetcode.com/problems/implement-stack-using-queues/discuss/381976/Python-solutions
#implementing stack using 2 queues
from collections import deque
class pop_costly_stack:
    def __init__(self):
        #initializing your data strucutre
        self.q1 = deque()
        self.q2 = deque()
        self._top = None
    def push(self,x):
        #push element x into stack
        self.q1.append(x)
        self._top = x
    def pop():
        #remove element on top of stock and returns the element
        while len(self.q1) > 1:
            self._top = self.q1.popleft()
            self.q2.append(self._top)
        result = self.q1.popleft()
        #swapping queues
        self.q1,self.q2 = self.q2,self.q1
        return result
    def top(self):
        #getting the top element
        return self._top
    def empty(self):
        """
        returns whether stack is empty or not
        """
        return len(self.q1) == 0





#push costly
class push_costly_stack:
    def __init__(self):
        #initializing your data strucutre
        self.q1 = deque()
        self.q2 = deque()
        self._top = None
    def push(self,x):
        #push element x into stack
        self.q2.append(x)
        self._top = x
        while self.q1:
            self.q2.append(self.q1.popleft())
        #swapping
        self.q1,self.q2 = self.q2,self.q1
    def pop():
        #remove element on top of stock and returns the element
        result = self.q1.popleft()
        while self.q1:
            self._top = self.q1[0]
        return result

    def top(self):
        #getting the top element
        return self._top
    def empty(self):
        """
        returns whether stack is empty or not
        """
        return len(self.q1) == 0



# Single queue
class single_queue:
    def __init__(self):
        #initializing your data strucutre
        self.q = deque()

    def push(self,x):
        #push element x into stack
        tmp = deque([x])
        tmp.extend(self.q)
        self.q = tmp
    def pop():
        #remove element on top of stock and returns the element
        return self.q.popleft()

    def top(self):
        #getting the top element
        return self.q[0]
    def empty(self):
        """
        returns whether stack is empty or not
        """
        return len(self.q) == 0
















#
