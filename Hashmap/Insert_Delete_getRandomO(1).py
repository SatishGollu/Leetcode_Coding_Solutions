# Brute - O(n)
class RandomizedSet:
    import random

    def __init__(self):
        self.array = []
        

    def insert(self, val: int) -> bool:
        if val not in self.array:
            self.array.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.array:
            self.array.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
class RandomizedSet:
    # optimized one
    import random

    def __init__(self):
        # declaring data structures
        self.dict = {}
        self.list = []       

    def insert(self, val: int) -> bool:
        """
        Insert a value to the set, Returns true if the set did not
        already contain the specified element
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True        

    def remove(self, val: int) -> bool:
        """
        Remove a value from the set, Return true if the set contains the
        specific element
        """
        if val in self.dict:
            #move the last element to the place idx of the element
            last_element = self.list[-1]
            index = self.dict[val]
            
            self.list[index],self.dict[last_element] = last_element,index
            #delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        return False
            
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()