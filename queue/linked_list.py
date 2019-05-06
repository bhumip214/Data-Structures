class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        # wrap the value in a new node 
        new_node = Node(value)
        # 1. what if our Linked List is empty?
        # how do we even check if our linked list if empty?
        if not self.head and not self.tail: 
            # if our list if empty, then the node that we add to
            # the list needs to be set as both the head and the tail
            self.head = new_node
            self.tail = new_node
        # 2. what if our linked list is not empty
        else:
            # add to the tail of the list
            # update the tail node's next_node reference to point to the new node
            self.tail.set_next(new_node)
            #don't forget to update the linked list's self.tail reference 
            self.tail = new_node 
    
    def remove_head(self):
        #1. what if our linked list if empty?
        if not self.head and not self.tail:
            return None
        
        #2. what if our linked list has one node?
        # how do we check if our linked list has one node?
        if self.head == self.tail:
        # we can also check if self.head.next points to None ==> if not self.head.get_next():
            old_head = self.head
            #now we can go ahead and set both head and tail to None
            self.head = None
            self.tail = None
            return old_head.get_value()
    
        #3. what if our linked list has more than one node?
        else: 
            # set the list's head reference to refer to the head node's next node
            old_head = self.head
            self.head = self.head.get_next()
            return old_head.get_value()

    def contain(self, value):
        # make sure we have elements in the list to traverse
        if not self.head and not self.tail:
            return None
        current = self.head

        # keep traversing while we're at a valid node
        while current:
            if current.get_value() == value:
                return True
            # update our current pointer
            current = current.get_next()
        #we've tranversed the entire list and none of the list nodes
        #have the value we're looking for, return false
        return False 
