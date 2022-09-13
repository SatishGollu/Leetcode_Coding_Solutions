# A SINGLE NODE OD A SINGLY LINKED LIST
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


# A LINKED LIST CLASS WITH A SINGLE HEAD NODE
class LinkedList:
    def __init__(self):
        self.head = None
        
        # ADD FIRST    
    def add_first(self, new_data): 
        # Create a new node
        new_node = Node(new_data)       
        # Make next of new Node as head 
        new_node.next = self.head 
        #Move the head to point to new Node  
        self.head = new_node 

    # Traversing  
    def __iter__(self):
        node = self.head
        while node is not None:
                yield node
                node = node.next
        
      # Add LAST
    def add_last(self, new_data):
        # Create a new node 
        new_node = Node(new_data) 
       # If the Linked List is empty, then make the new node as head 
        if self.head is None: 
                self.head = new_node 
                return
       # Else traverse till the last node 
        last = self.head 
        while (last.next): 
                last = last.next
       #Change the next of last node 
        last.next =  new_node 

    # INSERTING BEFORE    
    def insert_before(self, target_node_data, new_node):
        # If the linked list is empty
        if not self.head:
            raise Exception("List is empty")
        # Add a node before the head
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        # Treverse to find the target node
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        # Target node is not present
        raise Exception("Node with data '%s' not found" % target_node_data)
    
    
    # INSERTING'AFTER'
    def insert_after(self, target_node_data, new_node):
        # If the linked list is empty
        if not self.head:
                raise Exception("List is empty")
        #Trevese to find the target node
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        # Target node is not present
        raise Exception("Node with data '%s' not found" % target_node_data)
    
    # DELETE A NOTE
    def delete_node(self, target_node_data):
        #If the list is empty
        if not self.head:
            raise Exception("List is empty")
        #If the target node is the head
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        #Treverse to find the target node
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
        #Target node is not present
        raise Exception("Node with data '%s' not found" % target_node_data)
    
    
    
        # Utility function to print the linked list 
    def printList(self): 
        temp = self.head 
        nodes = []
        while temp is not None: 
            nodes.append(temp.data)
            temp = temp.next
        nodes.append("Null")
        return  " -> ".join(nodes)
    


#Execition start here
if __name__=='__main__': 
    # Start with the empty list 
    llist = LinkedList() 
    # Insert a.  Linked list becomes a>Null
    llist.add_first("a") 
    # Insert b at the beginning. Linked list become b->a->Null
    llist.add_first("b")
    # Insert e at last. Linked list becomes b->a->e->Null
    llist.add_last("e"); 
    #Insert aa after a. Linked list becomes b->a->aa->e->Null
    llist.insert_after("a", Node("aa")) 
     #Insert aa before e. Linked list becomes b->a->aa->ee->e->Null
    llist.insert_before("e",Node("ee"))
    # Delete node aa
    llist.delete_node("aa")
  
    print(llist.printList())
