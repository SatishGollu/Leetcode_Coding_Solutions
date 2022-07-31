# with arrays
class MyHashMap:
    def __init__(self):
        self.data = [None] * 100001
    def put(self,key,val):
        self.data[key] = val
    def get(self,key):
        val = self.data[key]
        return val if val != None else 1
    def remove(self,key):
        self.data[key] = None

#with hash using multiplication hashing
class MyHashMap:
    #used trick for fast bit operation modulo 2^t: 
    #for any s: s % (2^t) = s & (1<<t) - 1.
    def eval_hash(self,key):
        return ((key*1031237) & (1<<15)-1)>>5

    def __init__(self):
        self.array = [[] for _ in range(1<<15)]
        
    def put(self, key: int, value: int) -> None:
        t = self.eval_hash(key)
        for i,(k,v) in enumerate(self.array[t]):
            if k == key:
                self.array[t][i] = (k,value)
                return
        self.array[t].append((key,value))    

    def get(self, key: int) -> int:
        t = self.eval_hash(key)
        for i,(k,v) in enumerate(self.array[t]):
            if k == key:
                return v
        return -1
    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        for i,(k,v) in enumerate(self.array[t]):
            if k == key:
                self.array[t].remove((k,v))

#Time - All complexities are the same: it is O(1) in average
#  if we assume that probability of collision is small.
'''
Complexity: easy question is about space complexity: it is O(2^15), 
because this is the size of our list. We have a lot of empty 
places in this list, but we still need memory to allocate this 
list of lists. Time complexity is a bit tricky. If we assume, 
that probability of collision is small, than it will be in 
average O(1). However it really depends on the size of our 
self.arr. If it is very big, probability is very small. 
If it is quite tight, it will increase. For example if we 
choose size 1000000, there will be no collisions at all, 
but you need a lot of memory. So, there will always be 
trade-off between memory and time complexity.
'''