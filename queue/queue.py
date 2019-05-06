class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  # should add an item to the back of the queue
  def enqueue(self, item):
    self.storage.append(item)  
  
  # should remove and return an item from the front of the queue
  def dequeue(self):
    if len(self.storage) == 0:
      return None
    else:
      return self.storage.pop(0)

  # returns the number of items in the queue
  def len(self):
    return len(self.storage)
