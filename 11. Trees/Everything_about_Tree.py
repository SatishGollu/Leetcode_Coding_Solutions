from collections import deque
from re import A
from unittest import result
class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None

    #insert left

    def insert_left(self,value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    #insert right
    def insert_right(self,value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node
    # DFS tree traversals.
    def pre_order(self):
        print(self.value)

        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()
    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.value)

        if self.right_child:
            self.right_child.in_order()


    def post_order(self):
        if self.left_child:
            self.left_child.post_order()

        if self.right_child:
            self.right_child.post_order()
        print(self.value)
    #BFS tree traversals
    def bfs(self):
        q = deque()
        q.appendleft(self)

        while q:
            current_node = q.pop()
            print(current_node)

            if current_node.left_child:
                q.appendleft(current_node.left_child)
            if current_node.right_child:
                q.appendleft(current_node.right_child)


class Binary_Search_Tree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self,value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = Binary_Search_Tree(value)

        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = Binary_Search_Tree(value)

    def find_node(self,value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)

        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        return value == self.value
    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None


    def remove_node(self,value,parent):
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value,self)
        elif value < self.value:
            return False
        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value,self)

        elif value > self.value:
            return False
        else:
            if self.left_child is None and self.right_child is None and self == parent.left_child:
                parent.left_child=None
                self.clear_node()
            elif self.left_child is None and self.right_child is None and self == parent.right_child:
                parent.right_child = None
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.left_child:
                parent.left_child = self.left_child
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.right_child:
                parent.right_child = self.left_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.left_child:
                parent.left_child = self.right_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.right_child:
                parent.right_child = self.right_child
                self.clear_node()
            else:
                self.value = self.right_child.find_minimum_value()
                self.right_child.remove_node(self.value, self)

            return True


    def find_minimum_value(self):
        if self.left_child:
            return self.left_child.find_minimum_value()

        else:
            return self.value
    




if __name__ == "__main__":
    a_node = BinaryTree(3)
    a_node.insert_left(5)
    a_node.insert_right(1)

    a_node.left_child.insert_left(6)
    a_node.left_child.insert_right(2)
    a_node.left_child.left_child.insert_left(None)
    a_node.left_child.left_child.insert_right(None)
    a_node.left_child.right_child.insert_left(7)
    a_node.left_child.right_child.insert_right(4)
    a_node.left_child.right_child.left_child.insert_left(None)
    a_node.left_child.right_child.left_child.insert_right(None)
    a_node.left_child.right_child.right_child.insert_left(None)
    a_node.left_child.right_child.right_child.insert_right(None)

    a_node.right_child.insert_left(0)
    a_node.right_child.left_child.insert_left(None)
    a_node.right_child.left_child.insert_right(None)
    a_node.right_child.insert_right(8)
    a_node.right_child.right_child.insert_left(None)
    a_node.right_child.right_child.insert_right(None)


    print(BinaryTree.pre_order(a_node))
