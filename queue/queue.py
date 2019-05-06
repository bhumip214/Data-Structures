import sys
from linked_list import LinkedList

# Implemented using Linked List
class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  # should add an item to the back of the queue
  def enqueue(self, item):
    self.storage.add_to_tail(item) 
    self.size += 1 
  
  # should remove and return an item from the front of the queue
  def dequeue(self):
    if self.size == 0:
      return None
    else:
      self.size -= 1
      return self.storage.remove_head()

  # returns the number of items in the queue
  def len(self):
    return self.size


#Implemented using Python List
# class Queue:
#   def __init__(self):
#     self.size = 0
#     # what data structure should we
#     # use to store queue elements?
#     self.storage = []

#   # should add an item to the back of the queue
#   def enqueue(self, item):
#     self.storage.append(item)  
  
#   # should remove and return an item from the front of the queue
#   def dequeue(self):
#     if len(self.storage) == 0:
#       return None
#     else:
#       return self.storage.pop(0)

#   # returns the number of items in the queue
#   def len(self):
#     return len(self.storage)
