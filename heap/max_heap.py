class Heap:
  def __init__(self):
    self.storage = []

  # adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  # removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed.
  def delete(self):
    self.storage[0], self.storage[len(self.storage) - 1] = self.storage[len(self.storage) - 1], self.storage[0]
    topmost_value = self.storage.pop()
    self._sift_down(0) 
    return topmost_value

  # returns the maximum value in the heap in constant time.
  def get_max(self):
    return self.storage[0]
  
  # returns the number of elements stored in the heap.
  def get_size(self):
    return len(self.storage)

  # moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index
  # the index parameter is the index of the node wherever it is in the array 
  def _bubble_up(self, index):
    # loop until either the element reaches the top of the array
    # or we'll break thhe loop when we realize the element's priority
    # is not larger than its parent's value
    while index > 0:
      # the value at 'index' fetches the index of its parent
      parent = (index - 1) // 2
      # check if the element at 'index' has priority than the elemts at the parent index
      if self.storage[index] > self.storage[parent]:
        # then we need to swap the elements
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        # we also need to update the index
        index = parent
      else: 
        # otherwise, our element has reached a spot in the heap where its parent 
        # element had higher priority; stop climbing
        break

  # grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent.
  def _sift_down(self, index):
    largest = index
    l = (2 * index) + 1
    r = (2 * index) + 2
    
    # Check if left child exists and its value is greater than root value
    if l < self.get_size() and self.storage[l] > self.storage[largest]:
        largest = l 
  
    # Check if right child exists and its value is greater than root value
    if r < self.get_size() and self.storage[r] > self.storage[largest]:  
        largest = r 
  
    # Check if index of largest value is not same as the index of root value
    if largest != index: 
        # swap 
        self.storage[index], self.storage[largest] = self.storage[largest], self.storage[index] 
        # keep recursing until both largest and index matches 
        self._sift_down(largest) 
  
    