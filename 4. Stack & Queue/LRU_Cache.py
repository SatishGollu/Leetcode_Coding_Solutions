#using doubly LinkedList and dictionary

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self,capacity:int):
        #key to node
        self.dic = dict()
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self,node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    def _remove(self,node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def put(self,key,value):
        if key in self.dic:
            self._remove(self.dic[key])
            del self.dic[key]
        elif len(self.dic) == self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]
        #adding item to lru LRUCache
        n = Node(key,value)
        self.dic[key] = n
        self._add(n)

    def get(self,key):
        if key in self.dic == False:
            return -1
        n = self.dic[key]
        self._remove(n)
        self._add(n)
        return n.val



""" we can also implement by using ordered dict and deque"""

#using deque - TLE
from collections import deque

class LRUCache:
    def __init__(self,capacity:int):
        self.capacity = capacity
        self.deque = deque()

    def _find(self,key:int):
        for i in range(len(self.deque)):
            n = self.deque[i]
            if n[0] == key:
                return i
            else:
                return -1

    def put(self,key:int,value:int):
        indx = self._find(key)
        if indx == -1:
            if len(self.deque) > = self.capacity:
                self.deque.popleft()
            self.deque.append((key,value))
        else:
            del self.deque[indx]
            self.deque.append((key,value))

    def get(self,key:int):
        indx = self._find(key)
        if indx == -1:
            return -1
        else:
            k,v = self.deque[indx]
            del self.deque[indx]
            self.deque.append((k,v))
            return v



#using ordered dict
from collections import OrderedDict
class LRUCache:
    def __init__(self,capacity:int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self,key:int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
    def put(self,key:int,value:int)-> None:
        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            else:
                self.cache.move_to_end(key)
        self.cache[key] = value











#
